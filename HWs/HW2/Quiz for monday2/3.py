alphabe = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabe.split()
string = input()
for letter in string:

    if letter.lower() in alphabet: print(alphabet.index(letter.lower()) + 1, end = " ")