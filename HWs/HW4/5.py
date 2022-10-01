class Wordplay():
    list = ["word", "word1", "word2", "word3", "wordd", "words", "woow", "wdd"]
    def words_with_length(length):
        return [word for word in Wordplay.list if len(word) == length]

    def starts_with(begin):
        return [word for word in Wordplay.list if word[:len(begin)] == begin]

    def ends_with(end):
        return [word for word in Wordplay.list if word[-len(end):] == end]

    def palindromes():
        return [word for word in Wordplay.list if word[::-1] == word]

    def only(list):
        res = []
        for word in Wordplay.list:
            good = True
            for letter in word:
                if letter not in list:
                    good = False
            if good: res.append(word)
        return res

    def avoids(list):
        res = []

        for word in Wordplay.list:
            good = True
            for letter in word:
                if letter in list:
                    good = False
                    break
            if good: res.append(word)
        return res

print(Wordplay.words_with_length(5))
print(Wordplay.starts_with("wo"))
print(Wordplay.ends_with("d1"))
print(Wordplay.palindromes())
print(Wordplay.only(["w", "d"]))
print(Wordplay.avoids(['1']))

