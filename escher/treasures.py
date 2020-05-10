def treasures(info, limit):
    keys = sorted(info.keys(), key = lambda k: info[k]['weight'] / info[k]['price'])
    limit *= 1000
    tres = ['golden coin', 'silver coin', 'ruby']
    for k in keys:
        d = min(info[k]['amount'], int(limit) // info[k]['weight'])
        info[k].setdefault('bag', d)
        limit -= info[k]['weight'] * d
    return [k + ': ' + str(info[k]['bag']) for k in tres if info[k]['bag']]