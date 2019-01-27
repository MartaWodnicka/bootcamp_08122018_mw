
class Product:
    """Opis produktów w sklepie"""
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        """Wypisanie informacji o produkcie"""
        print(f"Produkt {self.nazwa}, id: {self.id} , cena: {self.cena} PLN")

    def __str__(self):
        return f"<Produkt nazwa: {self.nazwa}, id: {self.id}>"


produkt = Product(1, "Woda", 2.99)
produkt.print_info()

print(help(produkt))



