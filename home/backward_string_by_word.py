def backward_string_by_word(text: str) -> str:
    return " ".join([i[::-1] for i in text.split(" ")])