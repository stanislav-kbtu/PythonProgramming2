import re

strings = input()
passwords = strings.split(",")
res = []
for password in passwords:
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[$#@]',password) and 6 <= len(password) <= 12:
       res.append(password)
       
print(", ".join(res))