def sum(list):
    res = 0
    for elem in list: res += elem
    return res

def mean(list):
    return sum(list) / len(list)

a = None
list = []
while a != 0:
    a = int(input())
    if a != 0: list.append(a)
print("Sum is: ", sum(list))
print("Mean is: ", mean(list))