def helper(a, p=0):
    k = a.index(min(a)) if a else 0
    r = ["%s%s" % (p+x-1, p+x) for x in range(k, 0, -1)]
    return r + helper(a[:k] + a[k+1:], p+1) if a else []
swapsort = lambda a: ','.join(helper(a, 0))