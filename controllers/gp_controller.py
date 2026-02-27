import json

from exceptions.not_found_exception import NotFoundException
from models.grands_prix.gp_dto import GrandPrixDto
from services.gp_service import GrandPrixService


class GrandPrixController:

    _instance = None
    _gp_service = None

    def __new__(cls):
        if not GrandPrixController._instance:
            cls._instance = super(GrandPrixController, cls).__new__(cls)
            cls._instance._gp_service = GrandPrixService()

        return cls._instance

    def resolve_request(self, event):
        method, path = tuple(event['routeKey'].split(" "))

        try:
            match method, path:
                case "GET", "/grands-prix/{year}":
                    return self.get_grands_prix_by_year(event['pathParameters']['year'])
                case "GET", "/grands-prix/{year}/{gp_id}":
                    return self.get_grand_prix_by_id(event['pathParameters']['year'], event['pathParameters']['gp_id'])
                case "PUT", "/grands-prix":
                    return self.upsert_grand_prix(json.loads(event['body']))
                case "DELETE", "/grands-prix/{year}/{gp_id}":
                    return self.delete_grand_prix(event['pathParameters']['year'], event['pathParameters']['gp_id'])
                case _:
                    return {"statusCode": 404}
        except NotFoundException as e:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": str(e)})
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"message": str(e)})
            }

    def get_grands_prix_by_year(self, year: int):
        return self._gp_service.list_grand_prix(year)

    def get_grand_prix_by_id(self, year: int, gp_id: str):
        return self._gp_service.get_grand_prix(year, gp_id)

    def upsert_grand_prix(self, gp_json):
        self._gp_service.put_grand_prix(GrandPrixDto(**gp_json))
        return {
            "statusCode": 201
        }

    def delete_grand_prix(self, year, gp_id):
        self._gp_service.delete_grand_prix(year, gp_id)
        return {
            "statusCode": 204
        }