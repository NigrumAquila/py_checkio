from itertools import accumulate
from operator import mul
from typing import Iterable

def reversed_permutation_index(length: int, index: int) -> Iterable[int]:
    digits = list(range(length))
    weights = reversed([1] + list(accumulate(range(1, length), mul)))
    index -= 1
    ret = []
    for w in weights:
        num, index = divmod(index, w)
        ret.append(digits.pop(num))
    return tuple(ret)