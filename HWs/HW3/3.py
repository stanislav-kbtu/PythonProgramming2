def checkforvowels(word):
    for vowel in vowels:
        if vowel not in word and vowel.upper() not in word: return False
    return True

import re 
with open("bigtext.txt", 'r') as f:
    text = f.read()
    pattern_for_words = r'[A-Za-z`]+'
    words = re.findall(pattern_for_words, text)

    pattern1 = r'ime$'
    pattern2 = r'[A-Za-z]ave'
    pattern3 = r'[rlstneRLSTNE]'
    pattern4 = r'[rlstnRLSTN]'
    pattern5 = r'[aeouiyAEOUYI]'
    vowelstring = "a e o u i y"
    ime = []
    ave = []
    rst = []
    withoute= []
    novowels = []
    containsvowels = []
    vowels = vowelstring.split()
    for word in words:
        if re.search(pattern1, word.lower()): 
            ime.append(word)
        if re.search(pattern2, word.lower()): 
            ave.append(word)
        if re.search(pattern3, word.lower()):
            rst.append(word)
            if 'e' not in word and 'E' not in word: withoute.append(word)
        if not re.search(pattern5, word): novowels.append(word)
        if checkforvowels(word): containsvowels.append(word)

        
    print("All words ending in 'ime':", *ime)
    print("All words with ave:", *ave)
    print("Count of words containing r, s, t, l, n, e:", len(rst))
    print("Percentage of words containing at least one of r, l, s, t, n:", (len(withoute) / len(words))* 100, "%")
    print("All words with no vowel:", *novowels)
    print("All words that contain every vowel:", *containsvowels)
        