a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

discriminant = b ** 2 -4 * a * c
if discriminant < 0: print("No real roots.")
else: 
    print((- b + pow(discriminant, 0.5))/ 2 * a )
    print((- b - pow(discriminant, 0.5))/ 2 * a )
