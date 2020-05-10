import re

def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace("*", "\\*").replace(".", "\\.").replace("[!", "[^").replace("[]", "[^.]").replace("[^]", "\[!\]")
    return re.match(pattern, filename) != None