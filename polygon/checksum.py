def checkio(data):
    res = sum(sum(divmod(n * 2, 10)) if i % 2 == 0 else n
        for i, n in enumerate(ord(c) - 48 for c in reversed(data) if c.isalnum()))
    final = str(10 * (res % 10 != 0) - (res % 10))
    return [final, res]