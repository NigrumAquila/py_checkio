sum_consecutives = lambda a, g=__import__("itertools").groupby: [sum(v) for _, v in g(a)]