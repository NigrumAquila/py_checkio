from typing import Iterable

def flood_area(diagram: str) -> Iterable[int]:
    incl = lambda c: { '_' : 0, '/' :  1, '\\' : -1 }[c]
    diag = [sum(map(incl, diagram[:i])) for i in range(len(diagram) + 1)]

    lmax = lambda n: min(max(diag[:n], default = 0), max(diag[n:], default = 0))
    vals = [max(0, lmax(n) - d) for (n, d) in enumerate(diag)]

    zero = [n for (n, m) in enumerate(vals) if not m]
    return [sum(vals[a:b]) for (a, b) in zip(zero, zero[1:]) if sum(vals[a:b])]