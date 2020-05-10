def highest_building(bs):
    return next((j+1, len(bs) - i) for i, r in enumerate(bs) for j, v in enumerate(r) if v)