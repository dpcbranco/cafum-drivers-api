from controllers.teams_controller import TeamsController

teams_controller = TeamsController()

def lambda_handler(event, context):
    return teams_controller.resolve_request(event)

if __name__ == "__main__":
    print(
        lambda_handler(
            {
                "version": "2.0",
                "routeKey": "DELETE /teams/{team_id}",
                "rawPath": "/path/to/resource",
                "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
                "headers": {
                    "Header1": "value1",
                    "Header2": "value1,value2"
                },
                "body": "eyJ0ZXN0IjoiYm9keSJ9",
                "pathParameters": {
                    "team_id": "sauber"
                },
                "stageVariables": {
                    "stageVariable1": "value1",
                    "stageVariable2": "value2"
                }
            },
            None
        )
    )