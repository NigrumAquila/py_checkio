from calendar import day_name, isleap, weekday

def most_frequent_days(year, names=list(day_name)):
    return sorted((day_name[weekday(year, 1, 1 + i)] for i in range(1 + isleap(year))), key=names.index)