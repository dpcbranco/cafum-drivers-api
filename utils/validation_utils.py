import re

def is_hex_color(s):
    pattern = re.compile(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$")
    return bool(pattern.match(s))