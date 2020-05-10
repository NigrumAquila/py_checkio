def hex_spiral(first, second):
    DIRS = ((0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1), (1, -1, 0))
    tiles = {1: (0, 0, 0), 2: (0, -1, 1)}
    loc = (0, -1, 1)
    lvl = 1
    dir_index = 2
    maxval = max(first, second)
    for val in range(3, maxval+1):
        nextloc = tuple(p+d for p, d in zip(loc, DIRS[dir_index]))
        if sum(abs(p) for p in nextloc) != 2*lvl:
            dir_index = (dir_index+1) % len(DIRS)
            turnloc = tuple(p+d for p, d in zip(loc, DIRS[dir_index]))
            if turnloc in tiles.values():
                loc = nextloc
                lvl += 1
            else:
                loc = turnloc
        else:
            loc = nextloc
        tiles[val] = loc
        
    return sum(abs(x-y) for x, y in zip(tiles[first], tiles[second])) // 2
