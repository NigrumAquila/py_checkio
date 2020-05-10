def create_intervals(data):
    numbers = sorted(data)
    left = None
    right = None
    for i in range(len(numbers)):
        if i == 0 or numbers[i]-numbers[i-1] > 1:
            left = numbers[i]
        if i == len(data)-1 or numbers[i+1]-numbers[i] > 1:
            right = numbers[i]
        if left and right:
            interval = (left, right)
            left = None
            right = None
            yield interval