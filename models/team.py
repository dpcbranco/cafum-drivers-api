import json

class Team:
    __pk: str = "TEAM"
    __sk: str
    __team_name: str
    __team_color: str

    def __init__(self, team_id, team_name, team_color):
        self.__sk = team_id
        self.__team_name = team_name
        self.__team_color = team_color

    def __str__(self):
        return json.dumps({
            "team_id": self.__sk,
            "team_name": self.__team_name,
            "team_color": self.__team_color
        })

    def __repr__(self):
        return self.__str__()

    def get_team_id(self):
        return self.__sk

    def get_team_name(self):
        return self.__team_name

    def get_team_color(self):
        return self.__team_color

    def set_team_name(self, team_name):
        self.__team_name = team_name

    def set_team_color(self, team_color):
        self.__team_color = team_color
