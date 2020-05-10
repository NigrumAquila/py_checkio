def stone_wall(wall):
    wall = list(zip(*wall.split())) 
    return min(range(len(wall)), key = lambda i: wall[i].count('#'))