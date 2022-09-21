n = int(input())
list = []
list.append(int(n / 100))
list.append(int((n - int(n / 100) * 100) / 10))
list.append(int(n % 10))
if list == sorted(list): print("YES")
else: print("NO")