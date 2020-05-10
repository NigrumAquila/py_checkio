from typing import List, Tuple

def distance(circles, i, j):
    dc = ((circles[i][0]-circles[j][0])**2 + (circles[i][1]-circles[j][1])**2)**0.5
    ri = (circles[i][2])
    rj = (circles[j][2])
    return (dc<ri+rj and ri<dc+rj and rj<dc+ri)

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    n = len(circles)
    color = [i+1 for i in range(n)]
    gr = 1
    
    for i in range(n):
        for j in range(i+1, n):
            if distance(circles, i, j):
                if color[i] != color[j]:
                    min_color = min(color[i], color[j])
                    max_color = max(color[i], color[j])
                    for k in range(n):
                        if color[k] == max_color:
                            color[k] = min_color
    return len(set(color))