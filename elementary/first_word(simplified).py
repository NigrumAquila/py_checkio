import string

def first_word(text: str) -> str:
    idx = text.find(' ') if len(text) != 0 else 0;
    if(idx != -1):
        return text[0:idx];
    return text[0:len(text)]