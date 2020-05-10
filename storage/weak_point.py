def weak_point(matrix):
    v = list(map(sum, matrix))
    h = [sum([i[j] for i in matrix]) for j in range(len(matrix[0]))]
    return [v.index(min(v)), h.index(min(h))]