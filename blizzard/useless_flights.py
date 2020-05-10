from typing import List
def useless_flight(schedule, magic=2):
    best = dict(sum([[((x, y), z), ((y, x), z)] for x, y, z in schedule], []))
    for _ in range(magic):
        for (a, b), (c, d) in [(x, y) for x in best for y in best if x != y]:
            if b != c: continue
            best.update({(a, d): min(best[(a, b)]+best[(c, d)], best.get((a, d), 1e9))})
    return [i for i, (a, b, p) in enumerate(schedule) if p > best[(a, b)]]