from typing import List
import math

def checkio(data: List[int]) -> [int, float]:
    data = sorted(data)
    if (len(data) % 2) != 1:
        x = data[math.floor(len(data) / 2) - 1]
        y = data[math.floor(len(data) / 2)]
        z = (y - x) / 2
        return x + z
    return data[math.floor(len(data) / 2)]