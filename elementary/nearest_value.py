def nearest_value(values: set, one: int) -> int:
    return min((abs(n-one), n) for n in values)[1]