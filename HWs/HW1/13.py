import datetime as dt


year = int(input("Input a year: "))
month = int(input("Input a month: "))
day = int(input("Input a day: "))
date = dt.date(year, month, day)
new = date + dt.timedelta(1)
print("The next date is:", new)