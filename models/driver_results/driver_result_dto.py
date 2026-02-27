from exceptions.invalid_exception import InvalidException


class DriverResultDTO:
    team_name: str
    team_color: str
    driver_name: str
    driver_number: int
    finished: bool

    def __init__(self, team_name, team_color, driver_name, driver_number, finished = True):
        self.team_name = team_name
        self.team_color = team_color
        self.driver_name = driver_name
        self.driver_number = int(driver_number)
        self.finished = finished
        self.__validate()

    def to_dict(self):
        return {
            "team_name": self.team_name,
            "team_color": self.team_color,
            "driver_name": self.driver_name,
            "driver_number": self.driver_number,
            "finished": self.finished
        }

    def __validate(self):
        errors = []
        if self.team_name is None:
            errors.append("Driver Result team name must not be None")

        if self.team_color is None:
            errors.append("Driver Result team color must not be None")

        if self.driver_name is None:
            errors.append("Driver Result driver name must not be None")

        if self.driver_number is None:
            errors.append("Driver Result driver number must not be None")
        elif self.driver_number < 0:
            errors.append("Driver Result driver number must not be negative")

        if errors:
            raise InvalidException(errors)