def checkio(first, second):
    return ','.join(sorted([i for i in first.split(',') if i in second.split(',')]))