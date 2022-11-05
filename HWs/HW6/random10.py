import random as rdm

def generate():
    sequence = [2, 2, 2, 2] + [rdm.choice([0, 1, 2]) for i in range(6)]
    rdm.shuffle(sequence)
    res = ""
    for num in sequence:
        res += rdm.choice(lists[num])
    return res

lower = [chr(i) for i in range(97, 123)]
upper = [chr(i) for i in range(65, 91)]
digits = "0 1 2 3 4 5 6 7 8 9".split()
lists = [lower, upper, digits]

print(generate())