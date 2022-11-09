import numpy as np
import random

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

password = generate()
print(password + " --> " + secret_password(password))
print(secret_password("mattedabi"))
print(secret_password("mubashirh"))
print(secret_password("HeLen-eda"))