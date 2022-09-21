n = list(map(int, input().split()))
n = sorted(n)
it = 0
for i in n:
    it += 1
    if i % 2 == 1: 
        print(i)
        break
    if it == 6: print("Not Found.")
