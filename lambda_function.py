from controllers.teams_controller import TeamsController

teams_controller = TeamsController()

def lambda_handler(event, context):
    return teams_controller.resolve_request(event)

if __name__ == "__main__":
    print(
        lambda_handler(
            {
                "version": "2.0",
                "routeKey": "PUT /teams",
                "rawPath": "/path/to/resource",
                "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
                "headers": {
                    "Header1": "value1",
                    "Header2": "value1,value2"
                },
                "body": "{\"team_id\":\"audi\",\"team_name\":\"Audi F1 Team\",\"team_color\":\"#BCC6CC\",\"first_driver\":{\"name\":\"Nico Hulkenberg\",\"number\":27},\"second_driver\":{\"name\":\"Gabriel Bortoleto\",\"number\":5}}",
                "pathParameters": {
                    "team_id": "audi"
                },
                "stageVariables": {
                    "stageVariable1": "value1",
                    "stageVariable2": "value2"
                }
            },
            None
        )
    )