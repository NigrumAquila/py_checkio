def checkio(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=abs)