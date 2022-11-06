def fibo(k):
    if k == 1 or k == 2: return 1
    return fibo(k - 1) + fibo(k - 2)

def C(list, a, b, collected):
    global solution
    solution = 1000000000
    rec(list, a, b, collected)
    return solution

def rec(list, a, b, collected):
    if len(list) == 1: 
        return collected
    global solution
    res = rec(list[:int(len(list)/2)], a, b, collected + b)
    if res != None: 
        if res < solution: solution = res
    res = rec(list[int(len(list)/2):], a, b, collected + a)
    if res != None: 
        if res < solution: solution = res

k = int(input("Enter your k: "))
print(130 * C(range(1, 1013), k, fibo(k), 0))
#print(C(range(1, 501), 2, 3, 0))