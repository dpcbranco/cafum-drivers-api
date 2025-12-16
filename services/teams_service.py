from connectors.dynamodb_connector import DynamoDBConnector
from boto3.dynamodb.conditions import Key

from exceptions.not_found_exception import NotFoundException
from models.team_dto import TeamDTO
from models.team_entity import TeamEntity


class TeamsService:

    _instance = None
    _table = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(TeamsService, cls).__new__(cls)
            cls._instance._table = DynamoDBConnector().get_table("cafum-bets-db")

        return cls._instance

    def list_teams(self):
        teams_query_return = self._table.query(
            Select='ALL_ATTRIBUTES',
            KeyConditionExpression=Key('pk').eq('TEAM')
        )

        return [
            TeamDTO(team_id=team_db["sk"], team_name=team_db["team_name"], team_color=team_db["team_color"])
            for team_db in teams_query_return["Items"]
        ]

    def get_team(self, team_id: str):
        team_entity = self._table.get_item(
            Key={'pk': "TEAM", "sk": team_id}
        ).get('Item')

        if not team_entity:
            raise NotFoundException(team_id)

        return TeamDTO(team_id=team_entity["sk"], team_name=team_entity["team_name"], team_color=team_entity["team_color"])

    def put_team(self, team: TeamEntity):
        db_response = self._table.put_item(Item=team.to_db_entity())
        return db_response