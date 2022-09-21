word = "EVAPORATE"
map = {}
for letter in word:
    map[letter] = "_"
finished = False
print("Welcome to Hangman!")
while not finished:
    letter = input("Guess your letter: ")
    if letter in word:
        map[letter] = True
        for letter in word:
            if map[letter] == True: print(letter, end = "")
            else: print("_", end = "")
        print("")


    else: print("Incorrect!")

    i = 0
    for value in map.values():
        if value == True:
            i += 1
    if i == len(map):
        print("Good job!")
        finished = True
