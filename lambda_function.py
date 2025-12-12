from controllers.teams_controller import TeamsController

teams_controller = TeamsController()

def lambda_handler(event, context):
    return teams_controller.get_teams()

if __name__ == "__main__":
    print(lambda_handler({"name": "Daniel"}, None))