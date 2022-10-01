class Product:
    products = []
    def __init__(self, n, a, p):
        self.products.append(self)
        self.name = n
        self.amount = a
        self.price = p

    def get_price(self, n):
        if n < 10:
            return self.price
        if 10 <= n <= 99: return self.price * 0.9
        else: return self.price * 0.8

    def make_purchase(self, n):
        if n <= self.amount: 
            return self.get_price(n) * n
        else: return False
potato = Product("Potato", 10, 20)
banana = Product("Banana", 20, 30)
orange = Product("Orange", 15, 25)
snickers = Product("Snickers", 100, 10)

for i in range(1):
    bill = {}
    for prod in Product.products:
        n = int(input(f'How many {prod.name.lower()}`s you wish to buy?\n'))
        print(prod.make_purchase(n))
        if prod.make_purchase(n) != False: 
            bill[prod.name] = [prod.get_price(n), n, prod.make_purchase(n)]
        else: 
            print(f'Amount of {prod.name} is {prod.amount}.' )
            n = int(input(f'How many {prod.name.lower()}`s you wish to buy?\n'))
            bill[prod.name] = [prod.get_price(n), n, prod.make_purchase(n)]

    print("\n\nTOTAL BILL----------")
    res = 0
    for key, value in bill.items():
        print(f'{key} : Price for 1 - {value[0]}$, Amount - {value[1]}, Price total - {value[2]}$')
        res += value[2]
    print(f'In total - {res}$')





