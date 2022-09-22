import itertools as it

def ana_str_str(target, sec):
    annags= []
    permutations = list(it.permutations(target))
    for permutation in permutations:
        annag = ""
        for letter in permutation:
            annag += letter
        annags.append(annag)
    for annag in annags:
        if annag in sec: return True
    return False



str1 = input()
str2 = input()
print(ana_str_str(str1, str2))