from typing import List, Tuple

def rectangles_union(recs: List[Tuple[int]]) -> int:
    return len({(i,j) for x0, y0, x1, y1 in recs
                      for i in range(x0, x1)
                      for j in range(y0, y1)})