def findall(string, letter):
    locations = []
    while True:
        pos = string.find(letter)
        if pos != -1:
            locations.append(pos)
            string.replace(letter, "", 1)
        else:
            return locations

s = input()
letter = input()
print(findall(s,letter))