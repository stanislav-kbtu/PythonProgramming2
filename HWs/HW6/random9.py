import random as rdm
lower = [chr(i) for i in range(97, 123)]
letter = rdm.choice(lower)
res = ""
for i in range(rdm.randint(1, 20)):
    res += letter
print(res)