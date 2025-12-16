import json

from exceptions.invalid_exception import InvalidException
from exceptions.not_found_exception import NotFoundException
from models.team_dto import TeamDTO
from services.teams_service import TeamsService


class TeamsController:

    _instance = None
    _teams_service = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(TeamsController, cls).__new__(cls)
            cls._instance._teams_service = TeamsService()

        return cls._instance

    def resolve_request(self, event):
        method, path = tuple(event["routeKey"].split(" "))

        try:
            match method, path:
                case "GET", "/teams":
                    return self.get_teams()
                case "GET", "/teams/{team_id}":
                    return self.get_team_by_id(event["pathParameters"]["team_id"])
                case "PUT", "/teams":
                    return self.create_update_team(json.loads(event["body"]))
                case "DELETE", "/teams/{team_id}":
                    return self.delete_team(event["pathParameters"]["team_id"])
                case _:
                    return {"statusCode": 404}
        except NotFoundException as e:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": str(e)})
            }

        except InvalidException as e:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": str(e)})
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"message": str(e)})
            }

    def get_teams(self):
        return {
            "statusCode": 200,
            "body": str(self._teams_service.list_teams())
        }

    def get_team_by_id(self, team_id):
        return {
            "statusCode": 200,
            "body": str(self._teams_service.get_team(team_id))
        }

    def create_update_team(self, team_json):
        self._teams_service.put_team(TeamDTO(**team_json))
        return {
            "statusCode": 201
        }

    def delete_team(self, team_id):
        self._teams_service.delete_team(team_id=team_id)
        return {
            "statusCode": 204
        }