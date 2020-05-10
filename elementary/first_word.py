import re
def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)