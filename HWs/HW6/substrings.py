def sum(string):
    res = 0
    for char in string: 
        res += int(char)
    return res

def isFriendly(string):
    dict = {}
    for i in range(len(string)): 
        dict[i] = False
    i, j = 0, 1
    while j in range(len(string)): 
        if sum(string[i:j+1]) == 10: 
            for n in range(i, j + 1): 
                dict[n] = True
            j += 1
        elif sum(string[i:j+1]) < 10: j += 1
        elif sum(string[i:j+1]) > 10: i += 1
    if False in dict.values(): 
        return False
    else: 
        return True



n = int(input())
count = 0
for string in range(9, (10 ** n) + 1):
    if isFriendly(str(string)): 
        print(string)
        count +=1

print(count)
