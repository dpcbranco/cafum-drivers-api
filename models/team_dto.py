import json

from botocore.exceptions import ValidationError

from exceptions.invalid_exception import InvalidException
from utils.validation_utils import is_valid_id, is_hex_color


class TeamDTO:
    team_id: str
    team_name: str
    team_color: str

    def __init__(self, team_id, team_name, team_color):
        self.team_id = team_id
        self.team_name = team_name
        self.team_color = team_color
        self.validate()

    def __str__(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return self.__dict__

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

        if errors:
            raise InvalidException(errors)