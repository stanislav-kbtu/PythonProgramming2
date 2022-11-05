import random as rdm

tickets = [rdm.randint(1000000000, 10000000000) for i in range(100)]
print("Lottery tickets are:", tickets)
for i in range(2): print("Winnet ticket is:", rdm.choice(tickets))