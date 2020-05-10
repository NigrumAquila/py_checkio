from typing import List
from math import gcd
from functools import reduce

def evenly_spaced_trees(trees: List[int]) -> int:
    gap = reduce(gcd, [trees[i + 1] - trees[i] for i in range(len(trees) - 1)])
    return (trees[-1] - trees[0]) // gap + 1 - len(trees)