def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

n = int(input())
if n <= 2: 
    result = 1 if n == 1 else 3
    print(result)
else: 
    result = 3
    for i in range(3, n +  1):
        result += i * 2 * factorial(n)
    print(result)
    
