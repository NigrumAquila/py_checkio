import re

def beginning_zeros(number: str) -> int:
    return len(re.sub(r'[^0].*$', '', number))