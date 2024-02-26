def is_year_leap(a):
    if a/4==int(a/4) and a/100!=int(a/100):
        return "true"
    else:
        return "false"


year = int(input("year: "))
b = is_year_leap(year)
print(b)