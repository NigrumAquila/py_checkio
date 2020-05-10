import functools


def checkio(number: int) -> int:
    return functools.reduce(lambda x,y:x*y, [int(char) for char in str(number) if not char == '0'])