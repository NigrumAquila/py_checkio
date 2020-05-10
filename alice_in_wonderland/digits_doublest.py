distance = lambda a, b: sum([a[i]!=b[i] for i in range(len(a))])

def checkio(numbers):
    paths = [[numbers.pop(0)]]
    while paths:
        current = paths.pop(0)
        for i in range(len(numbers) - 1, -1, -1):
            if distance(str(numbers[i]), str(current[-1])) != 1: continue
            if numbers[i] == numbers[-1]: return current+[numbers[-1]]
            paths.append(current+[numbers.pop(i)])