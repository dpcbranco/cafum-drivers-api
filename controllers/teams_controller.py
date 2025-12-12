from services.teams_service import TeamsService


class TeamsController:

    _instance = None
    _teams_service = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(TeamsController, cls).__new__(cls)
            cls._instance._teams_service = TeamsService()

        return cls._instance

    def get_teams(self):
        return self._teams_service.get_teams()