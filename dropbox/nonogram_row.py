def nonogram_row(line, groups):
    size, space = len(line), len(line)-sum(groups)-len(groups)+2
    combine = [["X"*i+"O"*g for i in range(space)] for i, g in enumerate(groups)]
    combine = map('X'.join, __import__('itertools').product(*combine))
    possible = [(i+'X'*size)[:size] for i in combine if len(i) <= size]
    possible = [x for x in possible if all(i+j not in 'OX,XO' for i, j in zip(line, x))]
    return ''.join([['?', x[0]][len(set(x)) == 1] for x in zip(*possible)]) or None