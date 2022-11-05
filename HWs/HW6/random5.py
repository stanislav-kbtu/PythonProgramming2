import random as rdm
#0 - lower, 1 - upper, 2 - special, 3 digit
def generate():
    sequence = [1, 1, 2, 3] + [rdm.choice([0, 1, 2, 3]) for i in range(6)]
    rdm.shuffle(sequence)
    password = ""
    for num in sequence:
        password += rdm.choice(lists[num])
    return password

lower = [chr(i) for i in range(97, 123)]
upper = [chr(i) for i in range(65, 91)]
special = "! @ ? # $ % ^ & * ( ) ".split()
digits = "0 1 2 3 4 5 6 7 8 9".split()

lists = [lower, upper, special, digits]

print(generate())