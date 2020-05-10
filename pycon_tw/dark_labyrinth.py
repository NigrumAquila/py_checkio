dom Review (?)
DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
PLAYER, WALL, UNKNOWN, EXIT, EMPTY = "P", "X", "?", "E", "."

class Map:
    def __init__(self, map):
        self.map = [list(row) for row in map]
        self.action = ''
    @property
    def dim(self):
        """Dimensions of self.map."""
        return len(self.map), len(self.map[0])

    def find_iter(self, what):
        """Generate coordinates of all 'what' elements."""
        yield from ((i, j) for i, row in enumerate(self.map)
                           for j, cell in enumerate(row)
                           if cell==what)
    def find(self, what) -> tuple:
        return next(self.find_iter(what), None)

    def update_dim(self, vision):
        Px, Py = self.find(PLAYER)
        self.map[Px][Py] = EMPTY
        n, s, w, e = [self.action.count(ch) for ch in 'NSWE']
        Px, Py = Px + s - n, Py + e - w
        self.map[Px][Py] = PLAYER
        VPx, VPy = vision.find(PLAYER)
        a, b = left_top_vision = (Px - VPx, Py - VPy)
        top, left = max(0, -a), max(0, -b)
        vr, vc = vision.dim
        right_bottom_vision = a + vr, b + vc
        sr, sc = self.dim
        c, d = a + vr - sr, b + vc - sc 
        bottom, right = max(0, c), max(0, d)
        for row in self.map:
            for k in range(left):
                row.insert(k, UNKNOWN)
            for k in range(right):
                row.append(UNKNOWN)
        nb_cols = self.dim[1]
        new_line = lambda: [UNKNOWN for k in range(nb_cols)]
        for k in range(top):
            self.map.insert(k, new_line())
        for k in range(bottom):
            self.map.append(new_line())
    def update(self, vision):
        self.update_dim(vision)
        vision.update_dim(self)
        for (i, j) in self.find_iter(UNKNOWN):
            self.map[i][j] = vision.map[i][j]

    def neighbors(self, coords, walls=False):
        i, j = coords
        r, c = self.dim
        allowed = (EMPTY, EXIT) if not walls else WALL
        for direction, (I, J) in DIR.items():
            if 0<=i+I<r and 0<=j+J<c and self.map[i + I][j + J] in allowed:
                yield direction, (i + I, j + J)
    def bfs(self, test) -> str:
        i, j = self.find(PLAYER)
        queue = [('',(i,j))]
        visited = {(i, j)}
        while queue:
            path, box = queue.pop(0)
            for direction, neighbor in self.neighbors(box):
                if test(neighbor):
                    return path + direction
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((path + direction, neighbor))
    def go_to(self, coords: tuple) -> str:
        return self.bfs(lambda x: x==coords)

    def point_of_interest(self, coords: tuple) -> bool:
        i, j = coords
        if self.map[i][j]==PLAYER:
            return False
        r, c = self.dim
        for line in [zip(range(i+1, r),      [j] * r),      
                     zip(range(i-1, -1, -1), [j] * r),      
                     zip([i] * c,            range(j+1, c)),
                     zip([i] * c,      range(j-1, -1, -1))]:
            for I, J in line:
                if self.map[I][J]==UNKNOWN:
                    return True # What is there?
                elif self.map[I][J] in WALL:
                    break 
            else:
                return True
        return False
    def explore(self) -> str:
        self.action = self.bfs(self.point_of_interest)
        return self.action
    __repr__ = __str__ = lambda self:'\n'.join(''.join(row) for row in self.map)


def find_path(visible):
    vision = Map(visible)
    if not hasattr(find_path, 'maze'):
        find_path.maze = vision
    else:
        find_path.maze.update(vision)
    coord_exit = find_path.maze.find(EXIT)
    if coord_exit:
        res = find_path.maze.go_to(coord_exit)
        del find_path.maze
        return res
    return find_path.maze.explore()