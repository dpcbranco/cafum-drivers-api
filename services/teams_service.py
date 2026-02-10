from boto3.dynamodb.conditions import Key

from connectors.dynamodb_connector import DynamoDBConnector
from exceptions.not_found_exception import NotFoundException
from models.teams.team_dto import TeamDTO
from models.teams.team_entity import TeamEntity
from utils.conversion_utils import team_dto_to_entity, team_entity_to_dto


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
        team_entity_dict = self._table.get_item(
            Key={'pk': "TEAM", "sk": team_id}
        ).get('Item')

        if not team_entity_dict:
            raise NotFoundException(team_id)

        return team_entity_to_dto(TeamEntity(**team_entity_dict))

    def put_team(self, team: TeamDTO):
        self._table.put_item(Item=team_dto_to_entity(team).to_dict())

    def delete_team(self, team_id: str):
        self._table.delete_item(Key={'pk': "TEAM", "sk": team_id})