from typing import Iterable

def replace_last(items: list) -> Iterable:
    return items[-1:] + items[:-1]