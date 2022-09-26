import re

with open("filenames.txt", "r") as f:
    initials = input()
    lines = f.readlines()
    pattern = r'\s?[A-Z]'
    
    list = [re.findall(pattern, line) for line in lines]
    for i in range(len(list)):
        if list[i][0] == initials[0] and list[i][len(list[i]) - 1] .strip() == initials[1]: print(lines[i], end = "")