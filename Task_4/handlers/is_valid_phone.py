import re

def is_valid_phone(phone):
    pattern = r'^\+?\d{10,15}$'
    return bool(re.fullmatch(pattern, phone))
