ns = list(map(int, input().split()))

if ns[1] + ns[0] == ns[2] or abs(ns[1] - ns[0]) == ns[2]: print("yes")
else: print("no")
