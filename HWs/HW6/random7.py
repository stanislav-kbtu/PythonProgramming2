import random as rdm

list = [i + 1 for i in range(6)]

state = rdm.getstate() 

for i in range(5):
    rdm.setstate(state)
    print(f'number {i + 1} roll: {rdm.choice(list)}')
print(rdm.choice(list))
print(rdm.choice(list))
