def correct_sentence(text):
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")