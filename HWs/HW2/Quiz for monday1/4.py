def check(pattern, L):
    res = []
    for string in L:
        matched = True
        for i in range(8):
            if string[i] != pattern[i] and pattern[i] != "*": 
                matched = False
        if matched: res.append(string)

    return res

L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

pattern = input()
print(check(pattern, L))

