from typing import Iterable

def except_zero(items: list) -> Iterable:
    it = iter(sorted(filter(None, items)))
    return [next(it) if i else 0 for i in items]