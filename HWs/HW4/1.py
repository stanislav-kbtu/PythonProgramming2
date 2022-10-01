class Investment():
    
    def __init__(self, p, i):
        self.principal = p
        self.interest = i

    def value_after(self, n):
        return self.principal * (self.interest + 1) * n

    def __str__(self):
        return f'Principal - {self.principal}$, Interest rate - {self.interest}%'

my = Investment(100, 3)

print(my.value_after(2))
print(my)