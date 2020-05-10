from collections import Counter

def frequency_sort(items):
    return [item for items, c in Counter(items).most_common() for item in [items] * c]
