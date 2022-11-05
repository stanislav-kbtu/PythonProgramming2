import random as rdm

letters = "! @ # $ % ^ & * ( )".split()
res = ""
for i in range(rdm.randint(1, 20)):
    res += rdm.choice(letters)
print(res)