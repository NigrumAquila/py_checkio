from collections import deque

def area(x, y, matrix):
    if matrix[y][x] == 0: return [0, 0]
    mx, my = len(matrix[0]), len(matrix)
    n = matrix[y][x]
    q = deque([(x, y)])
    count = 0
    while len(q) != 0:
        x, y = q.popleft()
        if matrix[y][x] != n: continue
        matrix[y][x] = 0
        count += 1
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < mx and 0 <= y1 < my: q.append((x1, y1))
    return [count, n]

def checkio(matrix):
    return max(area(x, y, matrix) for y in range(len(matrix)) for x in range(len(matrix[0])))