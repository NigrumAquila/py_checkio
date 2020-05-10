from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items