import json

from exceptions.invalid_exception import InvalidException
from utils.validation_utils import is_valid_id


class TeamEntity:
    pk: str = "TEAM"
    sk: str
    team_name: str
    team_color: str

    def __init__(self, team_name, team_color, sk = None):
        self.sk = sk
        self.team_name = team_name
        self.team_color = team_color
        self.validate()

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return self.__dict__

    def validate(self):
        errors = []
        if self.pk is None or self.pk is not "TEAM":
            errors.append("Team PK must be 'TEAM'")

        if self.sk is None:
            errors.append("Team SK is required")
        elif not is_valid_id(self.sk):
            errors.append("Team SK is invalid")

        if errors:
            raise InvalidException(errors)