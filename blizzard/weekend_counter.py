from datetime import date, timedelta


def checkio(from_date, to_date):
    return len([1 for d in range((to_date - from_date).days + 1) if (from_date + timedelta(d)).weekday() in [5, 6]])