import numpy as np
import random as rdm

def recursion(nested, level, search):
    count = 0
    for elem in nested:
        if type(elem) != type(4): 
            recursion(elem, level + 1, search)
        else:
            if elem == search: count += 1

    print("Level -", level, "  Count -",count)



nested = ([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
recursion(nested[0], 0, nested[1])

