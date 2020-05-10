def create_intervals(data):
    res = sorted(x for x in data for i in [-1, 1] if x + i not in data)
    return [(x, y) for x, y in zip(res[::2], res[1::2])]