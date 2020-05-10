def reverse_ascending(items):
    run, current = [], -float('inf')
    for element in items:
        if element > current:
            run.append(element)
            current = element
        else:
            yield from run[::-1]
            run, current = [element], element
    yield from run[::-1]