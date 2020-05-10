from typing import Iterable

def remove_all_after(items: list, border: int) -> Iterable:
    return items[:items.index(border)+1] if border in items else items