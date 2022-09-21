string = input()
dict = {}
for i in string:
    if i not in dict.keys(): dict[i] = 1
    else: dict[i] += 1 

for key, value in dict.items():
    print(key, " - ", value)