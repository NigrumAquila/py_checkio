from itertools import chain

def flat_list(x):
    if isinstance(x, list):
        yield from chain.from_iterable(map(flat_list, x))
    else: yield x