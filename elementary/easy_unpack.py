def easy_unpack(tup: tuple) -> tuple:
    size = len(tup);
    res = (tup[0], tup[2], tup[size - 2],);
    return res;