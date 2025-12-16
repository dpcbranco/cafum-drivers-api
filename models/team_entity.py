import json

class TeamEntity:
    pk: str
    sk: str
    team_name: str
    team_color: str

    def __init__(self, team_name, team_color, team_id = None, sk = None, pk:str="TEAM"):
        self.pk = pk
        self.sk = sk if sk is not None else team_id
        self.team_name = team_name
        self.team_color = team_color

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def to_db_entity(self):
        return self.__dict__