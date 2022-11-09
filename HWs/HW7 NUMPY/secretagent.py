import numpy as np
import re
import random

alph = {}
s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)): alph[i + 1] = s[i]


def generate():
	return "".join([random.choice([chr(j) for j in range(97, 123)]) for i in range(9)])

def secret_password(password):
	if len(password) != 9: return "BANG! BANG! BANG!"
	for char in password: 
		if char not in [chr(j) for j in range(97, 123)]: return "BANG! BANG! BANG!"
	list = [password[i*3:i*3 + 3] for i in range(3)]
	list[1] = list[1][-1::-1]
	part1 = f'{ord(list[0][0]) - 96}{list[0][1]}{ord(list[0][2]) - 96}'
	list[0] = part1
	part3 = ""	
	for char in list[2]: 
		part3 += chr(ord(char) + 1) if char != 'z' else 'a'
	list[2] = part3
	return list[1] + list[2] + list[0] 

def decode(code):
	part1 = re.findall(r'([a-z]{3}$|\d.*$)', code)[0]
	digs = re.findall(r'\d+', part1)
	let = re.sub(r'\d*(.)\d*', r"\1", part1)
	part1 = alph[int(digs[0])] + let + alph[int(digs[1])]
	part3 = ""
	for elem in code[3:6]:
		part3 += alph[ord(elem) - 96 - 1] if elem != 'a' else 'z'
	part2 = ""
	for i in range(3):
		part2 += code[:3][-(i + 1)]
	return part1 + part2 + part3
	
password = generate()
print(password + " --> " + secret_password(password))
print(secret_password("mattedabi"))
print(secret_password("mubashirh"))
print(secret_password("HeLen-eda"))
print(decode(secret_password("mubashirh")))		
print(decode(secret_password("mattedabi")))