from datetime import datetime, timedelta


def vacation(date, days):
    rd = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=days)
    if rd.weekday() > 4:
        rd += timedelta(days=(7-rd.weekday()))
    return str(rd.date())