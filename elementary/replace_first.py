from typing import Iterable

def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1]