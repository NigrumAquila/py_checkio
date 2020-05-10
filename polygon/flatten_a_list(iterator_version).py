def flat_list(l):
    for x in l: yield from [x] if isinstance(x, int) else flat_list(x)