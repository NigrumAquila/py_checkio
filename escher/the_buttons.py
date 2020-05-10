def buttons(ceiling):
    connections = ((1, 0), (0, 1), (0, -1), (-1, 0))
    g = [[int(c) for c in line] for line in ceiling.strip().splitlines()]
    sizex, sizey = len(g), len(g[0])
    visited = set()

    def is_new(x, y):
        return (x, y) not in visited and 0 <= x < sizex and 0 <= y < sizey and g[x][y] != 0

    def sum_connected(x, y):
        nonlocal visited
        active = [(x, y)]
        visited.add((x, y))
        s = 0
        while active:
            x, y = active.pop()
            s += g[x][y]
            neighbors = {(x + dx, y + dy) for dx, dy in connections if is_new(x + dx, y + dy)}
            active += neighbors
            visited |= neighbors
        return s

    buttons = (sum_connected(x, y) for x in range(sizex) for y in range(sizey) if is_new(x, y))
    return sorted(buttons, reverse=True)