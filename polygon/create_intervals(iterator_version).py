def create_intervals(data):
    try: first, *data = sorted(data)
    except ValueError: return
    last = first
    for current in data:
        if last + 1 < current:
            yield first, last
            first = current
        last = current
    yield first, last