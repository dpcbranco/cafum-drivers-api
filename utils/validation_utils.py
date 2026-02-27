import collections
import re

from exceptions.invalid_exception import InvalidException
from models.driver_results.driver_result_dto import DriverResultDTO


def is_hex_color(s):
    pattern = re.compile(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$")
    return bool(pattern.match(s))

def is_valid_id(s):
    pattern = re.compile(r"^[a-z0-9]{3,20}$")
    return bool(pattern.match(s))

def check_event_result_errors(event_results: dict[str, DriverResultDTO]) -> list:
    errors = []
    missing_positions = []
    used_driver_numbers = []
    repeated_drivers = []
    invalid_keys = []

    for key in event_results.keys():
        if not key.isdigit():
            invalid_keys.append(key)

    for i in range(1, event_results.__len__() + 1):
        position = str(i)
        if position not in event_results:
            missing_positions.append(i)

        else:
            driver_number = event_results[position].driver_number
            if driver_number in used_driver_numbers:
                repeated_drivers.append(driver_number)
            else:
                used_driver_numbers.append(driver_number)


    if len(missing_positions) > 0:
        errors.append(f"Missing positions: {missing_positions}")

    if len(repeated_drivers) > 0:
        errors.append(f"Repeated drivers: {repeated_drivers}")

    if len(invalid_keys) > 0:
        errors.append(f"Invalid keys: {invalid_keys}")

    return errors