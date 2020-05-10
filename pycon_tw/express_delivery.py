from heapq import *
def checkio(field):  
    h = []
    heappush(h, [0, True, 0, 0, ''])
    v = set()
    
    while True:
        t, b, r, c, s = heappop(h)
        if r < 0 or r >= len(field) or c < 0 or c >= len(field[r]):
            continue
        if field[r][c] == 'W' or (b, r, c) in v:
            continue
        if field[r][c] == 'E' and b:
            return s
        v.add((b, r, c))
        
        if field[r][c] == 'B':
            heappush(h, [t + 1, not b, r, c, s + 'B'])
            
        for dr, dc, ds in [[0, -1, 'L'], [0, 1, 'R'], [1, 0, 'D'], [-1, 0, 'U']]:
            heappush(h, [t + 1 + int(b), b, r + dr, c + dc, s + ds])