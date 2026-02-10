import json

from exceptions.invalid_exception import InvalidException
from models.drivers.driver_dto import DriverDTO
from utils.validation_utils import is_valid_id, is_hex_color


class TeamDTO:
    team_id: str
    team_name: str
    team_color: str
    first_driver: DriverDTO
    second_driver: DriverDTO

    def __init__(self, team_id, team_name, team_color, first_driver=None, second_driver=None):
        self.team_id = team_id
        self.team_name = team_name
        self.team_color = team_color
        self.first_driver = DriverDTO(**first_driver) if first_driver else None
        self.second_driver = DriverDTO(**second_driver) if second_driver else None
        self.validate()

    def __str__(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "team_color": self.team_color,
            "first_driver": self.first_driver.to_dict() if self.first_driver else None,
            "second_driver": self.second_driver.to_dict() if self.second_driver else None
        }

    def validate(self):
        errors = []
        if self.team_id is None:
            errors.append("Team ID is required")
        elif not is_valid_id(self.team_id):
            errors.append("Team ID is invalid")

        if self.team_name is None:
            errors.append("Team name is required")

        if self.team_color is None:
            errors.append("Team color is required")
        elif not is_hex_color(self.team_color):
            errors.append("Team color is invalid")

        if self.first_driver and self.second_driver:
            if self.first_driver.name == self.second_driver.name:
                errors.append("First driver and second driver have the same name")

            if self.first_driver.number == self.second_driver.number:
                errors.append("First driver and second driver have the same number")

        if errors:
            raise InvalidException(errors)