import re

list = input().split(", ")
print(list)

for number in list:
    if re.search(r'([+]7|8)\s?[-]?\d\d\d\s?[-]?\d\d\d\s?[-]?\d\d\s?[-]?\d\d', number): print("YES")
    else: print("NO")
