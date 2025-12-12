from connectors.dynamodb_connector import DynamoDBConnector
from boto3.dynamodb.conditions import Key

from models.team import Team


class TeamsService:

    _instance = None
    _table = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(TeamsService, cls).__new__(cls)
            cls._instance._table = DynamoDBConnector().get_table("cafum-bets-db")

        return cls._instance

    def get_teams(self):
        teams_query_return = self._table.query(
            Select='ALL_ATTRIBUTES',
            KeyConditionExpression=Key('pk').eq('TEAM')
        )

        return [
            Team(team_id=team_db["sk"], team_name=team_db["team_name"], team_color=team_db["team_color"])
            for team_db in teams_query_return["Items"]
        ]