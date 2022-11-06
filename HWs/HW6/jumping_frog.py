total_counter = 0
temp_counter = 0
def f(path, n): #path = [1]
    if len(path) == n:
        if path[-1] == n: return path
        else: pass

    pos = path[len(path) - 1]

    for i in range(pos - 3, pos + 3 + 1):

        if 2 <= i <=n and i not in path: 

            res = f(path + [i], n)
            if res != None: 
                
                global temp_counter
                temp_counter += 1

n = int(input())
for i in range(1, n + 1):
    f([1], i)
    total_counter += temp_counter ** 3
    temp_counter = 0

print(total_counter)
