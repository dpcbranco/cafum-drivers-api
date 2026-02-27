import json


class GrandPrixEntity:
    pk: str
    sk: str
    name: str
    quali_bet_limit_date: str
    race_bet_limit_date: str
    quali_result: dict
    race_result: dict

    def __init__(self, sk, name, quali_bet_limit_date, race_bet_limit_date, pk = None, year = None, quali_result = None, race_result = None):
        self.pk = f"RACE#{year}" if not pk else pk
        self.sk = f"{sk}"
        self.name = name
        self.quali_bet_limit_date = quali_bet_limit_date
        self.race_bet_limit_date = race_bet_limit_date
        self.quali_result = quali_result
        self.race_result = race_result

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "pk": self.pk,
            "sk": self.sk,
            "name": self.name,
            "quali_bet_limit_date": self.quali_bet_limit_date,
            "race_bet_limit_date": self.race_bet_limit_date,
            "quali_result": self.quali_result,
            "race_result": self.race_result
        }