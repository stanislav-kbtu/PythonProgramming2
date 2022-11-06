# Let`s construct triangle bounded by lines y = 3/2x, y = -x + 3, y = -2
import itertools as it
import numpy as np

eps = 0.01

def isInterior(x, y):
    if y - (3/2)*x < 0 and y + x -3 < 0 and y > -2: return True
    else: return False

def isBoundary(x, y):
    if (abs(y - (3/2)*x) <= eps and y + x -3 < 0 and y > -2) or ( y - (3/2)*x < 0 and abs(y + x -3) <= eps and y > -2) or ( y - (3/2)*x < 0 and y + x -3 < 0 and abs(y + 2) <= eps):
        return True
    else: return False

counter = 0

def isGood(array_of_points, P):
    print(array_of_points, P)

class Triangle():
    area = 12.09

    def __init__(self):
        self.points = []
        self.boundaries = []
        for i in np.arange(-1.8, 5, 0.1):
            for j in np.arange(-2.2, 2, 0.1):
                if isInterior(i, j): self.points.append((i, j))

                elif isBoundary(i, j): self.boundaries.append((i, j))
                elif abs((3/2)*i - j) < 0.1: self.boundaries.append((i, j))

def psi(n):
    #for point in triang.points:
    counter = 0
    for P in triang.points:

        for comb in it.combinations(triang.boundaries, n): 
            if isGood(list(comb), P): counter += 1



triang = Triangle()
print(len(triang.boundaries))
print(psi(3))