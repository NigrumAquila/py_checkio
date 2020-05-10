import numpy as np
from itertools import product

BLOCKS = {
    'T': {(0, 0), (0, 1), (0, 2), (1, 1)},
    'I': {(0, 0), (1, 0), (2, 0), (3, 0)},
    'O': {(0, 0), (0, 1), (1, 0), (1, 1)},
    'L': {(0, 0), (1, 0), (2, 0), (2, 1)},
    'J': {(0, 1), (1, 1), (2, 0), (2, 1)},
    'S': {(0, 1), (0, 2), (1, 0), (1, 1)},
    'Z': {(0, 0), (0, 1), (1, 1), (1, 2)},
}


def identify_block(tile):
    grid = np.arange(1, 17).reshape((4, 4))
    for (name, coords), r in product(BLOCKS.items(), range(4)):
        grid = np.rot90(grid)
        tile_coord = {(x, y) for x, y in product(range(4), repeat=2) if grid[x, y] in tile}
        if len(set((b[0] - t[0], b[1] - t[1]) for b, t in zip(sorted(coords), sorted(tile_coord)))) == 1:
            return name