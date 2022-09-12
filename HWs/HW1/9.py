string = "January, February, March, April, May, June, July, August, September, October, November, December"
months = string.split(", ")
month = int(input("Input the month (e.g. [1-12]): "))
day = input("Input the day: ")
season = "fall"
if months[month - 1] in months[:2] or months[month - 1] == "December": season = "winter" 
elif months[month - 1] in months[2:5]: season = "spring"
elif months[month - 1] in months[5:8]: season = "summer"
print(f'Output: {months[month - 1]}, {day}. Season is {season}.')
