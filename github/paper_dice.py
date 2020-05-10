def paper_dice(paper):
    cells = {(x, y): int(value) for y, row in enumerate(paper)
                                for x, value in enumerate(row) if value != ' '}
    
    def rotate(cube, s):
        sx, sy = s
        return {((-z * sx, y, x * sx), (x, -z * sy, y * sy))[sy != 0]: value
                for (x, y, z), value in cube.items()}
        
    def mark(cube, pos):
        cube[(0, 0, 1)] = cells[pos]
        del cells[pos]
        for s in (1, 0), (-1, 0), (0, 1), (0, -1):
            new_pos = pos[0] + s[0], pos[1] + s[1]
            if new_pos in cells:
                cube = rotate(mark(rotate(cube, s), new_pos), (-s[0], -s[1]))
        return cube
    
    cube = mark({}, next(iter(cells)))
    return (len(cube) == 6 and
            cube[(1, 0, 0)] + cube[(-1, 0, 0)] ==
            cube[(0, 1, 0)] + cube[(0, -1, 0)] ==
            cube[(0, 0, 1)] + cube[(0, 0, -1)] == 7)