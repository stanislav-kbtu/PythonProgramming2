months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
    }

import re

date = input(">>> Enter the date: ")
for month in months.keys():
    if month[:3].lower() in date.lower(): 

        res1 = f'{months[month]}/' + re.sub(r'.*[0]?\d?(\d).*\d\d(\d\d)', r'\1/\2', date)
        print(res1)
