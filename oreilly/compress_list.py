from itertools import groupby
from typing import Iterable

def compress(items: list) -> Iterable:
    return [k for k,g in groupby(items)]