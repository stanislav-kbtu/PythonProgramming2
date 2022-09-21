def test(w1, w2):
    dict = {}
    for i in range(len(w1)):
        if w2[i] in dict.values():
            if w1[i] in dict.keys():
                if dict[w1[i]] == w2[i]: continue
                else: return False
            else: return False
        else:
            dict[w1[i]] = w2[i]
    return True


word1 = input()
word2 = input()
if len(word1) != len(word2): print("Can`t be encoded.")
else: 
    if test(word1, word2) and test(word2, word1): print("Can be encoded.")
    else: print("Can`t be encoded.")
