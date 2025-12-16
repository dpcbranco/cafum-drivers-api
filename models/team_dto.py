import json


class TeamDTO:
    team_id: str
    team_name: str
    team_color: str

    def __init__(self, team_id, team_name, team_color):
        self.team_id = team_id
        self.team_name = team_name
        self.team_color = team_color

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()