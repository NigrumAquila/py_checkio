def power_supply(network, power_plants):
    out = {x for y in network for x in y}
    queue = list(power_plants.items())
    for k, v in ((x, y) for x, y in queue if y >= 0):
        queue += [(j if k == i else i, v-1) for i, j in network if k in (i, j)]
        out -= {k}
    return out