def index_power(array: list, n: int) -> int:
    try:
        return pow(array[n], n);
    except IndexError:
        return -1;