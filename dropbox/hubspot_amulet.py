from itertools import product
 
def checkio(matrix):
    for a in list(product(range(-180, 180, 45), repeat = 3)):
        if [sum(matrix[y][x] * a[y] for y in range(3)) % 360 for x in range(3)] == [0, 225, 315]:
            return a