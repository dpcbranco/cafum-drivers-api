from unittest import case

from controllers.gp_controller import GrandPrixController
from controllers.teams_controller import TeamsController

teams_controller = TeamsController()
gp_controller = GrandPrixController()

def lambda_handler(event, context):
    entity_path = event["rawPath"].split("/")[1]
    match entity_path:
        case "teams":
            return teams_controller.resolve_request(event)
        case "grands-prix":
            return gp_controller.resolve_request(event)
        case _:
            return {"statusCode": 404}

if __name__ == "__main__":
    print(
        lambda_handler(
            {
                "version": "2.0",
                "routeKey": "GET /grands-prix/{year}/{gp_id}",
                "rawPath": "/grands-prix",
                "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
                "headers": {
                    "Header1": "value1",
                    "Header2": "value1,value2"
                },
                "body": "{\n    \"grand_prix_id\": \"bahrain\",\n    \"year\": 2026,\n    \"name\": \"Gulf Air Bahrain Grand Prix 2026\",\n    \"quali_bet_limit_date\": \"2026-04-11T09:30:00\",\n    \"race_bet_limit_date\": \"2026-04-12T12:00:00\",\n    \"quali_result\": {\n        \"1\": {\n            \"team_name\": \"Mercedes\",\n            \"team_color\": \"#00D2BE\",\n            \"driver_name\": \"George Russell\",\n            \"driver_number\": 63\n        },\n        \"2\": {\n            \"team_name\": \"Red Bull Racing\",\n            \"team_color\": \"#1E41FF\",\n            \"driver_name\": \"Max Verstappen\",\n            \"driver_number\": 3\n        },\n        \"3\": {\n            \"team_name\": \"Ferrari\",\n            \"team_color\": \"#DC0000\",\n            \"driver_name\": \"Charles Leclerc\",\n            \"driver_number\": 16\n        }\n    },\n    \"race_result\": {\n        \"1\": {\n            \"team_name\": \"Red Bull Racing\",\n            \"team_color\": \"#1E41FF\",\n            \"driver_name\": \"Max Verstappen\",\n            \"driver_number\": 3\n        },\n        \"2\": {\n            \"team_name\": \"Mercedes\",\n            \"team_color\": \"#00D2BE\",\n            \"driver_name\": \"George Russell\",\n            \"driver_number\": 63\n        },\n        \"3\": {\n            \"team_name\": \"Ferrari\",\n            \"team_color\": \"#DC0000\",\n            \"driver_name\": \"Charles Leclerc\",\n            \"driver_number\": 16\n        }\n    }\n}",
                "pathParameters": {
                    "year": "2026",
                    "gp_id": "bahrain"
                },
                "stageVariables": {
                    "stageVariable1": "value1",
                    "stageVariable2": "value2"
                }
            },
            None
        )
    )