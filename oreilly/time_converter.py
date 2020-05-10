def time_converter(time):
    h, m = time.split(':')
    pm, b12 = time.find(' p.m.') != -1, int(h) == 12
    result = '{}:{}'.format(str([[h, '00'][b12 and not (pm)], int(h) + 12][pm and not (b12)]).zfill(2), m.replace(' p.m.', '').replace(' a.m.', ''))
    return result