
def a():
    print("Jestem w funcji a")

    def b():
        print("Jestem w funcji b")

    def c():
        print("Jestem w funcji c")
    # print(locals())
    # print(globals())
    b()
    c()
    print('int wewnątrz', int())
    print('int wewnątrz', int("7"))



def loguj_uzycie(func):
    """To będzie dekorator.
    Wypisze tekst przed i po uruchomieniu funkcji"""

    def wrapper(*args, **kwargs):
        print("To się wykona przed")

        #print("To się wykona po")
        return f"Wynik: {func(*args, **kwargs)}"
    return wrapper

@loguj_uzycie
def potega(podstawa, wykladnik):
    wynik = podstawa ** wykladnik
    # print(wynik)
    return wynik

# potega = loguj_uzycie(potega)

def pobierz_dane():
    print("Pobrałem dane")

# print("Bez dekoratora")
# pobierz_dane()
#
# print("Udekorowanie")
# pobierz_dane = loguj_uzycie(pobierz_dane)
# pobierz_dane()




print(potega(2, 4))