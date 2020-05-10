from datetime import date

def friday(day):
    return (4 - date(*map(int, reversed(day.split('.')))).weekday()) % 7