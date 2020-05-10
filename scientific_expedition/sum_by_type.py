from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    return (''.join(x for x in items if isinstance(x, str)),
            sum(x for x in items if isinstance(x, int)))