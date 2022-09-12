month = "January, February, March, April, May, June, July, August, September, October, November, December"
days31 = [0, 2, 4, 6, 7, 9, 11]
months = month.split(", ")
days = "30"

print("List of months: January, February, March, April,May, June, July, August, September, October, November, December")

m = input("Input the name of Month: ")
if months.index(m) in days31: days = "31"
elif m == "February": days = "28/29"
print(f'No. of days: {days}')