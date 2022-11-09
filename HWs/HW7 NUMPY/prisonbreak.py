import numpy as np
import random as rdm

def generate():
    length = rdm.randint(3, 8)
    arr = [rdm.choice([0, 1]) for i in range(length)]
    return arr

def count(arr):
    counter = 0
    current = 1
    if arr[0] == 0: return counter
    else: 
        for i in range(len(arr)):
            if arr[i] == current: continue
            else: 
                current = 0 if current == 1 else 1
                counter += 1

    return counter + 1

arr = generate()
print(arr)
print(count(arr))
print(count([1, 1, 0, 0, 0, 1, 0]))
print(count([1, 1, 1]))
print(count([0, 0, 0]))
print(count([0, 1, 1, 1]))
