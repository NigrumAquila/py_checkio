def count_words(text: str, words: set) -> int:
    return len({word for word in words if word in text.lower()})