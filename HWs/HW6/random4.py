import random as rdm

def generate():
    res = ""
    for i in range(5): 
        res += rdm.choice(letters)
    return res

letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
print(generate())