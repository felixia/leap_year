
def check_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is a leap year")

    elif (year % 4 ==0) and (year % 100 != 0):
        print(f"{year} is a leap year")

    else:
        print(f"{year} is not a leap year")
check_leap_year(2020)
