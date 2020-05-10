def checkio(text: str) -> str:
    count = 0
    lower = text.lower()
    for c in lower:
        if c.isalpha():
            if lower.count(c) > count:
                most = c
                count = lower.count(c)
            elif lower.count(c) == count:
                if c < most:
                    most = c
                    count = lower.count(c)
    return most