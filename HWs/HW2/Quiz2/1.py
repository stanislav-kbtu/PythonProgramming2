import random
n = random.randint(1, 100)
for i in range(3):
    user = int(input("Your guess: "))
    if user == n: 
        print("BINGO!")
        break
    elif user < n: print("Your guess is fewer.")
    else: print("Your guess is bigger.")