import re

list = "+7 777 621 34 56, 87012345678, +7078904367, 87687686, 9-7014460411, 8-701-446-04-11".split(", ")
print(list)

for number in list:
    if re.search(r'([+]7|8)\s?[-]?\d\d\d\s?[-]?\d\d\d\s?[-]?\d\d\s?[-]?\d\d', number): print("YES")
    else: print("NO")
