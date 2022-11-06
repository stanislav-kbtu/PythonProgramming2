import numpy as np


def findS(N):
    solutions = []
    for i in range(int(np.sqrt(N)) + 1):

        for j in range(int(np.sqrt(N)) + 1):

            if int(j ** 2 + i ** 2) == N and (j, i) not in solutions: solutions.append((i, j))

    return solutions



N = [4 * i + 1 for i in range(38)]
sum = 0
for num in N:
    for solution in findS(num):
        sum += solution[0]

print(sum)

