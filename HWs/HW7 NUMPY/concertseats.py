import numpy as np

def check(arr):
    for row in arr:

        for i in range(1, len(row)):

            if row[i - 1] > row[i]: return False
    return True

arr = np.array([[1, 2, 3, 2, 1, 1,], [2, 4, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]])

tr = arr.transpose()

print(check(tr))