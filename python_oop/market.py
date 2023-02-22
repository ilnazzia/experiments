class Cart: 
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{gd.name}: {gd.price}' for gd in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

tv1 = TV('LG', 50000)
tv2 = TV('Samsung', 150000)
tbl = Table('Swagen', 10000)
lptp1 = Notebook('Apple', 150000)
lptp2 = Notebook('MSI', 100000)
cp = Cup('Ikea', 100)

cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(tbl)
cart.add(lptp1)
cart.add(lptp2)
cart.add(cp)