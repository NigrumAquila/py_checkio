from typing import Tuple
import math

def permutation_index(numbers: Tuple[int])->int:
    nums = []
    for index, num in enumerate(numbers):
        nums.append(num - sum([1 for x in numbers[:index+1] if x<num]))

    return sum([num * math.factorial(pos) for pos, num in zip(reversed(range(len(nums))), nums)])+1