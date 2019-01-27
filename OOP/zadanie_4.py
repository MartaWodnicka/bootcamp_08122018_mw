class BasketEntry:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity

    def report(self):
        return f'- {self.product.name} ({self.product.id}), cena: {self.product.price} x {self.quantity}\n'

class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity):

        # self.entries.append({'product': product, 'quantity': quantity})
        # sciezka z uzyciem listy
        # for position in self.entries:
        #     if position[0] == product:
        #         position[1] += quantity
        #         break
        # else:
        #     self.entries.append([product, quantity])
        #
        # def count_total_price(self):
        #     total = 0
        #     for e in self.entries:
        #         pr = e[0]
        #         total += pr.price * e[1]
        #     return total

        # sciezka z uzyciem nowej klasy
        basket_entry = BasketEntry(product, quantity)
        for be in self.entries:
            if be.product == product:
                be.quantity += quantity
                break
        else:
            self.entries.append(basket_entry)

    def count_total_price(self):
        total = 0
        for e in self.entries:
            total += e.count_price()
        return total

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for e in self.entries:
            report += e.report()
        report += f"W sumie: {self.count_total_price()}"
        return report
class Product:
    """Opis produktów w sklepie"""

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        """Wypisanie informacji o produkcie"""
        print(f"Produkt {self.name}, id: {self.id} , cena: {self.price} PLN")

    def __str__(self):
        return f"<Produkt nazwa: {self.name}, id: {self.id}>"


def test_basket_initialization():
    basket = Basket()
    assert basket.entries == []


def test_product_initialization():
    product = Product(1, "Woda", 10)
    assert product.id == 1
    assert product.name == "Woda"
    assert product.price == 10


def test_basket_add_product():
    basket = Basket()
    product = Product(1, "Woda", 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1


def test_basket_add_product_twice():
    basket = Basket()
    product = Product(1, "Woda", 10)
    basket.add_product(product, 5)
    basket.add_product(product, 3)
    assert len(basket.entries) == 1



def test_basket_count_total_price():
    basket = Basket()
    product1 = Product(1, "Woda", 10)
    product2 = Product(2, "Ogorki", 5)
    basket.add_product(product1, 5)
    basket.add_product(product2, 3)

    assert basket.count_total_price() == 5*10 + 3*5


def test_basket_generate_report():
    basket = Basket()
    product = Product(1, "Woda", 10.0)
    basket.add_product(product, 5)
    assert basket.generate_report() == """Produkty w koszyku:
- Woda (1), cena: 10.0 x 5
W sumie: 50.0"""