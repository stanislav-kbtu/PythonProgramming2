def decrypt(word): # sr sgeemsectea -> secret message
    groups = []
    amount = int(len(word)/n) if len(word) % n== 0 else int(len(word)/n) + 1
    for i in range(n):
        if i == n - 1: groups.append(word[i*amount:])
        else: groups.append(word[i*amount:(i + 1) * amount])
    res = ""

    for i in range(amount):

        for j in range(amount):
            try:
                res += groups[j][i]
            except Exception as e:
                continue

    return res



word = input()
n = int(input())
print(decrypt(word))
