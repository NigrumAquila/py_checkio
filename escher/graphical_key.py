def g_key(grid, max_path_len):
    if max_path_len == len(grid) * len(grid[0]):
        return sum(sum(row) for row in grid)

    max_total = 0
    bottom_right = (len(grid) - 1, len(grid[0]) - 1)

    def gen_path(path, total):
        nonlocal max_total
        cur = path[-1]
        remaining = max_path_len - len(path)

        if cur == bottom_right:
            max_total = max(total, max_total)
            return

        if len(path) < max_path_len:
            for i in range(cur[0] - 1, cur[0] + 2):
                if i < 0 or i >= len(grid):
                    continue
                for j in range(cur[1] - 1, cur[1] + 2):
                    if j < 0 or j >= len(grid[i]):
                        continue
                    if (i, j) in path:
                        continue
                    if max(bottom_right[0] - i, bottom_right[1] - j) > remaining:
                        continue
                    gen_path(path + [(i, j)], total + grid[i][j])

    gen_path([(0, 0)], grid[0][0])
    return max_total