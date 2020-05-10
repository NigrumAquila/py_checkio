def split_list(items: list) -> list:
    s = (len(items)+1) // 2
    return [items[:s],items[s:]]