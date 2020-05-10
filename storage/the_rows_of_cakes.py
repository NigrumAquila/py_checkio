from itertools import combinations

def inline(p0, p1, p2):
    v0 = p1[0] - p0[0], p1[1] - p0[1]
    v1 = p2[0] - p0[0], p2[1] - p0[1]
    return v0[0]*v1[1] - v0[1]*v1[0] == 0

def checkio(cakes):
    lines = set()
    for c0, c1 in combinations(cakes, 2):
        line = frozenset(tuple(c) for c in cakes if inline(c, c0, c1))
        lines.add(line)
    return sum(len(line)>=3 for line in lines)