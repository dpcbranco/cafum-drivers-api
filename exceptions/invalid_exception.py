class InvalidException(Exception):
    errors: list[str]

    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return f"Invalid request. Errors: {self.errors}"