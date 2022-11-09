import numpy as np
import random

def check_spot(mat, i, j):
    count = 0
    if i != 0 and i != 4 and j != 0 and j != 4:
        if mat[i][j + 1] == '#' and i in range(5) and j + 1 in range(5): 
            count +=1
        if mat[i + 1][j + 1] == '#' and i + 1 in range(5) and j + 1 in range(5): 
            count += 1
        if mat[i - 1][j + 1] == '#' and i - 1 in range(5) and j + 1 in range(5): 
            count +=1
        if mat[i + 1][j] == '#' and i + 1 in range(5) and j in range(5): 
            count +=1
        if mat[i - 1][j] == '#' and i- 1 in range(5) and j in range(5): 
            count +=1
        if mat[i][j - 1] == '#' and i in range(5) and j - 1 in range(5): 
            count +=1
        if mat[i + 1][j - 1] == '#' and i + 1 in range(5) and j - 1 in range(5): 
            count +=1
        if mat[i - 1][j - 1] == '#' and i - 1 in range(5) and j - 1 in range(5): 
            count +=1
    else:
        if i in range(5) and j + 1 in range(5): 
            if mat[i][j + 1] == '#':
                count +=1
        if i + 1 in range(5) and j + 1 in range(5): 
            if mat[i + 1][j + 1] == '#':
                count += 1
        if i - 1 in range(5) and j + 1 in range(5): 
            if mat[i - 1][j + 1] == '#': 
                count +=1
        if i + 1 in range(5) and j in range(5): 
            if mat[i + 1][j] == '#':
                count +=1
        if i- 1 in range(5) and j in range(5): 
            if mat[i - 1][j] == '#': count +=1
        if i in range(5) and j - 1 in range(5): 
            if mat[i][j - 1] == '#': count +=1
        if i + 1 in range(5) and j - 1 in range(5): 
            if mat[i + 1][j - 1] == '#': count +=1
        if i - 1 in range(5) and j - 1 in range(5): 
            if mat[i - 1][j - 1] == '#': count +=1

    return count


def generate():
    return np.array([[random.choice(["#", "-"]) for j in range(5)] for i in range(5)])

def transform(mat):
    for i in range(5):

        for j in range(5):
            if mat[i][j] == "#": continue
            else: mat[i][j] = check_spot(mat, i, j)


    return mat


#matrix = generate()
#print(transform(matrix))
print(transform(np.array([ 
  ["-", "-", "-", "-", "-"], 
  ["-", "-", "-", "-", "-"], 
  ["-", "-", "#", "-", "-"], 
  ["-", "-", "-", "-", "-"],  ["-", "-", "-", "-", "-"] 
])))
print(transform(np.array([ 

  ["-", "-", "-", "-", "#"], 

  ["-", "-", "-", "-", "-"], 

  ["-", "-", "#", "-", "-"], 

  ["-", "-", "-", "-", "-"], 

  ["#", "-", "-", "-", "-"] 

])))
print(transform(np.array([ 

  ["-", "-", "-", "#", "#"], 

  ["-", "#", "-", "-", "-"], 

  ["-", "-", "#", "-", "-"], 

  ["-", "#", "#", "-", "-"], 

  ["-", "-", "-", "-", "-"] 

])))