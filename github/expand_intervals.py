from typing import Iterable
from itertools import chain


def expand_intervals(items: Iterable) -> Iterable:
    return chain(*(range(item[0], item[1]+1) for item in items))