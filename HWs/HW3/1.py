import re

with open("students.txt", "r") as f:
    lines = f.readlines()
    global new_lines
    new_lines = []
    pattern = r'(?P<name>.*)(?P<else>\s.+@.*)(?P<number>\d\d\d-\d\d\d\d)'
    for line in lines:
        res = re.search(pattern, line)
        part = res.groups()

        name = list(map(str.capitalize, part[0].split()))
        part1 = " ".join(name)

        part2 = re.sub(r'(\d\d\d)-(\d\d\d\d)', r'301-\1-\2', part[2])
        new_lines.append(part1 + part[1] + part2)

with open("students2.txt", "x") as f:
    for line in new_lines: f.write(line + "\n")


        
        