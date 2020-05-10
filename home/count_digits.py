def count_digits(text: str) -> int:
    return sum([1 for c in text if c.isdigit()])