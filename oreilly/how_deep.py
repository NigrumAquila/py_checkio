def how_deep(structure):
    if isinstance(structure, (tuple, list)):
        return 1 + max(map(how_deep, structure), default=0)
    return 0