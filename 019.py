# Counting Sundays
# Problem 19

def is_leap(year):
    if year % 4 is not 0:
        return False
    elif year % 100 is not 0:
        return True
    elif year % 400 is not 0:
        return False
    else:
        return True

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sunday_count = 0
weekday = 0

for year in range(1900, 2001):
    if is_leap(year):
        months[1] = 29
    else:
        months[1] = 28

    for month in range(len(months)):
        for day in range(months[month]):
            weekday += 1
            if weekday == 7:
                if day == 0 and year > 1900:
                    sunday_count += 1
                weekday = 0

print(sunday_count)

