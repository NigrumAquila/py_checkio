def cheapest_flight(data, start, stop, path=''):
    if start == stop: return 0
    cf, is_valid = cheapest_flight, lambda x, y: x == start and y not in path
    yin  = [p+cf(data, b, stop, path+a) for a, b, p in data if is_valid(a, b)]
    yang = [p+cf(data, a, stop, path+b) for a, b, p in data if is_valid(b, a)]
    return min(yin+yang, default=1e9)*(min(yin+yang, default=1e9) <= 1e9)