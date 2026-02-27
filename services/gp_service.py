from boto3.dynamodb.conditions import Key

from connectors.dynamodb_connector import DynamoDBConnector
from exceptions.not_found_exception import NotFoundException
from models.grands_prix.gp_dto import GrandPrixDto
from models.grands_prix.gp_entity import GrandPrixEntity
from utils.conversion_utils import gp_entity_to_dto, gp_dto_to_entity


class GrandPrixService:
    _instance = None
    _table = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GrandPrixService, cls).__new__(cls)
            cls._instance._table = DynamoDBConnector().get_table("cafum-bets-db")
        return cls._instance

    def list_grand_prix(self, year: int):
        grand_prixes = self._table.query(
            Select='ALL_ATTRIBUTES',
            KeyConditionExpression=Key('pk').eq(f"RACE#{year}"),
        )

        return [
            gp_entity_to_dto(GrandPrixEntity(**gp_entity)).to_dict() for gp_entity in grand_prixes["Items"]
        ]

    def get_grand_prix(self, year: int, gp_id: str):
        grand_prix = self._table.get_item(Key={"pk": f"RACE#{year}", "sk": gp_id}).get("Item")
        if not grand_prix:
            raise NotFoundException(gp_id)
        return gp_entity_to_dto(GrandPrixEntity(**grand_prix)).to_dict()

    def put_grand_prix(self, gp: GrandPrixDto):
        self._table.put_item(Item=gp_dto_to_entity(gp).to_dict())

    def delete_grand_prix(self, year: int, gp_id: str):
        self._table.delete_item(Key={"pk": f"RACE#{year}", "sk": gp_id})