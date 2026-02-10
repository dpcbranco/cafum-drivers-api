from exceptions.invalid_exception import InvalidException
import json

class DriverDTO:
    name: str
    number: int

    def __init__(self, name, number):
        self.name = name
        self.number = int(number)
        self.validate()

    def __str__(self):
        return json.dumps({"name": self.name, "number": self.number})

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return self.__dict__

    def validate(self):
        errors = []
        if not self.name.strip():
            errors.append("Driver's name is null or empty")

        if not self.number:
            errors.append("Driver's number is null")
        elif self.number < 0:
            errors.append("Driver's number is negative")

        if errors:
            raise InvalidException(errors)