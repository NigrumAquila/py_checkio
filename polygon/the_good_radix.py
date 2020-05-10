def checkio(number):
    r = max(int(i, 36) for i in number) + 1
    while r < 37 and int(number, r) % (r-1):
        r += 1
    return r % 37