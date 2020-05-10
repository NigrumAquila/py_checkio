from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if(len(elements) == 0):
        return True
    check = elements[0];
    for key in elements:
        if(key != check):
            return False;
    return True;