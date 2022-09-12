string = "Monkey, Rooster, Dog, Pig, Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat"
signs = string.split(", ")

year = int(input("Input your birth year: "))
print(f'Your Zodiac sign: {signs[year % 12]}')