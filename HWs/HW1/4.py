vowel = "a i o y e u"
vowels = vowel.split()
letter = input("Input a letter of the alphabet: ")
which = "vowel" if letter in vowels else "consonant"
print(f'{letter} is a {which}.')