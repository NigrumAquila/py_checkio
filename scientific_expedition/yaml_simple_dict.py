def yaml(a):
    d = {}
    for line in a.splitlines():
        if line:
            k, v = line.split(': ', maxsplit=1)
            try:
                d[k] = int(v)
            except ValueError:
                d[k] = v
    return d