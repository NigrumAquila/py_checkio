def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num)[::-1].replace('0',' ').lstrip()) 