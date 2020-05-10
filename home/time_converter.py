def time_converter(time):
    if time == '00:00':
        return '12:00 a.m.'
    if int(time[:2] + time[3:]) > 1259:
        return str(int(time[:2]) % 12) + time[2:] + ' p.m.'
    if int(time[:2] + time[3:]) > 1159:
        return time + ' p.m.'
    if int(time[:2] + time[3:]) < 1000:
        return time[1:] + ' a.m.'
    return time + ' a.m.'