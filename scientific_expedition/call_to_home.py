def total_cost(calls):
    d = dict()
    for key, _, val in (line.split() for line in calls):
        d[key] = d.get(key, 0) + (int(val)+59)//60
    return sum(n + (n - 100) * (n > 100) for n in d.values())