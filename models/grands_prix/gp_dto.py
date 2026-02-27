from datetime import datetime
from typing import Any

from exceptions.invalid_exception import InvalidException
from models.driver_results.driver_result_dto import DriverResultDTO
from utils.validation_utils import check_event_result_errors


class GrandPrixDto:

    grand_prix_id: str
    year: int
    name: str
    quali_bet_limit_date: str
    race_bet_limit_date: str
    quali_result: dict[str, DriverResultDTO]
    race_result: dict[str, DriverResultDTO]


    def __init__(
            self,
            grand_prix_id: str,
            year: int,
            name: str,
            quali_bet_limit_date: str,
            race_bet_limit_date: str,
            quali_result: dict,
            race_result: dict
    ):
        self.grand_prix_id = grand_prix_id
        self.year = year
        self.name = name
        self.quali_bet_limit_date = quali_bet_limit_date
        self.race_bet_limit_date = race_bet_limit_date
        self.quali_result = {key: DriverResultDTO(**value) for key, value in quali_result.items()}
        self.race_result = {key: DriverResultDTO(**value) for key, value in race_result.items()}
        self.__validate()

    def to_dict(self) -> dict:
        return {
            'grand_prix_id': self.grand_prix_id,
            'year': self.year,
            'name': self.name,
            'quali_bet_limit_date': self.quali_bet_limit_date,
            'race_bet_limit_date': self.race_bet_limit_date,
            'quali_result': {key: value.to_dict() for key, value in self.quali_result.items()},
            'race_result': {key: value.to_dict() for key, value in self.race_result.items()},
        }


    def __validate(self):
        errors = []
        if not self.grand_prix_id:
            errors.append('Grand Prix id cannot be empty')

        if self.year is None:
            errors.append('Grand Prix year cannot be empty')
        elif self.year < 2026:
            errors.append('Grand Prix year cannot be less than the current year')

        if self.name is None:
            errors.append('Grand Prix name cannot be empty')

        if self.quali_bet_limit_date is None:
            errors.append('Grand Prix quali_bet_limit_date cannot be empty')
        else:
            try:
                datetime.fromisoformat(self.quali_bet_limit_date)
            except ValueError:
                errors.append('Grand Prix invalid date format for quali_bet_limit_date')

        if self.race_bet_limit_date is None:
            errors.append('Grand Prix race_bet_limit_date cannot be empty')
        else:
            try:
                datetime.fromisoformat(self.race_bet_limit_date)
            except ValueError:
                errors.append('Grand Prix invalid date format for race_bet_limit_date')

        if self.quali_result:
            errors.extend([f"Grand Prix qualifying result error: {error}" for error in check_event_result_errors(event_results=self.quali_result)])

        if self.race_result:
            errors.extend([f"Grand Prix race result error: {error}" for error in check_event_result_errors(event_results=self.race_result)])

        if errors.__len__() > 0:
            raise InvalidException(errors)