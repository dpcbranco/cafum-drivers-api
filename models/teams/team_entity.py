import json

from exceptions.invalid_exception import InvalidException
from utils.validation_utils import is_valid_id


class TeamEntity:
    pk: str
    sk: str
    team_name: str
    team_color: str
    first_driver: dict
    second_driver: dict

    def __init__(self, team_name, team_color, sk, pk=None, first_driver=None, second_driver=None):
        self.pk = "TEAM" if pk is None else pk
        self.sk = sk
        self.team_name = team_name
        self.team_color = team_color
        self.first_driver = first_driver
        self.second_driver = second_driver
        self.validate()

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "pk": self.pk,
            "sk": self.sk,
            "team_name": self.team_name,
            "team_color": self.team_color,
            "first_driver": self.first_driver,
            "second_driver": self.second_driver
        }

    def validate(self):
        errors = []

        if self.sk is None:
            errors.append("Team SK is required")
        elif not is_valid_id(self.sk):
            errors.append("Team SK is invalid")

        if errors:
            raise InvalidException(errors)