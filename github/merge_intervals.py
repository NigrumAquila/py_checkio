import functools

def merge_intervals(intervals):
    def merge(res, x):     
        return res + [x] if not res or x[0] > res[-1][1] + 1 else res[:-1] + [(res[-1][0], max(x[1], res[-1][1]))]
    return functools.reduce(merge, intervals, [])