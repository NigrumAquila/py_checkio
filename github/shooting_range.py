def shot(w1, w2, sp, lp):
    f = lambda a, b, c, d: (b[1]-a[1])*(d[0]-c[0]) - (b[0]-a[0])*(d[1]-c[1])
    d, n, k = f(sp, lp, w1, w2), f(sp, lp, w1, lp), f(w1, w2, w1, sp)
    return round(min(200*n/d, 200-200*n/d))if d and 0<=n/d<=1 and k/d>=0 else -1