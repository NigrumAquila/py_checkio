def checkio(data: list) -> list:
    l = []
    for c in data:
        if data.count(c) != 1:
            l.append(c)
    return l