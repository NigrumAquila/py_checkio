def max_digit(number: int) -> int:
    return max([int(digit) for digit in list(str(number))])