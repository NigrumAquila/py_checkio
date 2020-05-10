from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    out = els[0:2]
    for i in range(2, len(els)):
        out.append(sorted(els[i-2:i+1])[1])
    return out