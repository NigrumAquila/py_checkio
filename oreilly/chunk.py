def chunking_by(items, n):
    for i in range(0, len(items), n):
        yield items[i:i + n]