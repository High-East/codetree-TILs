MONTH_LAST_DAY = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

SEASON = [0, "Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall", "Fall", "Fall", "Winter"]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def get_season(year, month, day):
    last_day = MONTH_LAST_DAY[month]
    if month == 2 and is_leap_year(year):
        last_day = 29
    if day > last_day:
        return -1
    return SEASON[month]

Y, M, D = map(int, input().split())
print(get_season(Y, M, D))