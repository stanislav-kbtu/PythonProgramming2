n = int(input())
list = []
for i in range(n):
    s = input()
    list.append(s)

def rotate(list):
    list.reverse()
    print(list[0: 1] + list[len(list) - 1: 0 : -1])

rotate(list)