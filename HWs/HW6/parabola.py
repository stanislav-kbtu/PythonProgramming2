import numpy as np
import itertools as it

def norm(vector):
    return np.sqrt((dotproduct(vector, vector))) 

def dotproduct(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]

def has45deg(point1, point2, point3):
    eps = 0.0000001
    if np.abs(anglebetween(point1, point2, point3) - np.pi/4) <= eps or abs(anglebetween(point2, point1, point3) - np.pi/4) <= eps or abs(anglebetween(point3, point2, point1) - np.pi/4) <= eps:
        #print(anglebetween(point1, point2, point3), anglebetween(point2, point1, point3), anglebetween(point3, point2, point1))
        return True
    else: return False

def anglebetween(point1, point2, point3):
    P2P1 = (point2[0] - point1[0], point2[1] - point1[1])
    P3P1 = (point3[0] - point1[0], point3[1] - point1[1])
    den = norm(P3P1) * norm(P2P1)
    try:
        cosangle = dotproduct(P2P1, P3P1)/den
        return np.arccos(cosangle)
    except: 
        return 0


K = input("Input range for coefficient k: ")
X = input("Range boundary X: ")
points = []
for k in range(1, int(K) + 1):
    for number in np.arange(-int(X), int(X), 1):
        points.append((number, (number ** 2) * (1/k)))
res = 0

for triple in it.combinations(points, 3):
    if has45deg(triple[0], triple[1], triple[2]): 
        #print("found", triple)
        res +=1

print(res)