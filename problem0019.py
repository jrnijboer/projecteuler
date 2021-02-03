def isLeapYear(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    return False

M = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 1900
day = 0
month = 1
sundayFirsts = 0
while year < 2001:
    day += 7
    if day > M[month - 1] or (month == 2 and isLeapYear(year)):
        day -= M[month - 1]
        if month == 2 and isLeapYear(year):
            day -= 1
        month += 1
        if month > 12:
            month -= 12
            year += 1
    if day == 1 and 1901 <= year <= 2000:
        sundayFirsts += 1
print(sundayFirsts)
