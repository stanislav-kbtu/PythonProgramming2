a = int(input("a: "))
b = int(input("b: "))
print(f'Area is {a * b / 2}.')
c = pow((a ** 2 + b ** 2), 1/2)  
print(f'Perimeter is {a + b + c}.')
print(f'Hypotenuse is {c}.')