def reduce(options):
    from copy import deepcopy
    result = deepcopy(options)
    for case in options:
        for visibles, blocks, banned in options[case]:
            for case1 in options:
                if all(visibles & b or blocks & v or blocks & d 
                       for v, b, d in options[case1]):
                    result[case].remove((visibles, blocks, banned))
                    break
    return result

def initialize(grid, cells, height, width, digits):
    from itertools import product
    from collections import defaultdict
    result = defaultdict(list)
    for x, y in digits:
        south = [{(x+i, y) for i in range(j)} for j in range(1, height-x+1)]
        north = [{(x-i, y) for i in range(j+1)} for j in range(x+1)]
        east = [{(x, y+i) for i in range(j)} for j in range(1, width-y+1)]
        west = [{(x, y-i) for i in range(j+1)} for j in range(y+1)]
        for s, n, e, w in product(*[range(len(z)) for z in (south, north, east, west)]):
            if len(south[s])+len(north[n])+len(east[e])+len(west[w])-3 != grid[x][y]:
                continue
            visibles = south[s] | north[n] | east[e] | west[w]
            blocks = {(x+len(south[s]), y), (x-len(north[n]), y)}
            blocks |= {(x, y+len(east[e])), (x, y-len(west[w]))}
            banned = [{(i+1, j), (i-1, j), (i, j+1), (i, j-1)} for i, j in blocks]
            banned = set.union(*banned) & cells
            result[(x, y)] += [(visibles, blocks & cells, banned)]
    prev, result = None, reduce(result)
    while prev != result:
        prev, result = result, reduce(result)
    return result

def are_cells_separated(cells, blocked):
    not_visited = cells-blocked
    stack = [next(iter(not_visited))]
    while stack:
        x, y = stack.pop()
        if (x, y) in not_visited:
            not_visited -= {(x, y)}
            neighbors = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} & cells
            stack += list(neighbors)
    return bool(not_visited)

def visibilities(grid):
    height, width  = len(grid), len(grid[0])
    cells = {(x, y) for x in range(height) for y in range(width)}
    digits = {(x, y) for x, y in cells if grid[x][y] != 0}
    options = initialize(grid, cells, height, width, digits)
    stack = [(set(), set(), digits)]
    while stack:
        blocked, seen, unsolved = stack.pop()
        if are_cells_separated(cells, blocked):
            continue
        if not unsolved:
            return blocked
        x, y = unsolved.pop()
        valid = [(see, block) for see, block, _ in options[(x, y)]
                 if not see & blocked and not block & seen]
        for see, block in valid:
            stack += [(blocked | block, seen | see, set(unsolved))]