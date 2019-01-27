liczby = [1, 2, 3, 4]
liczby2 = [5, 6, 7, 8]
liczby3 = [9, 16, 17, 18]


#for i, l in enumerate(liczby):
#    print(f'Indeks={i}, Wartość ={l}')

#for i, l in enumerate(liczby2):
#    print(f'Indeks={i}, Wartość ={l}')

#for i, l in enumerate(liczby3):
#    print(f'Indeks={i}, Wartość ={l}')

def drukuj(lista):
    for i, l in enumerate(lista):
        print(f'Indeks={i}, Wartość ={l}')

drukuj(liczby)
drukuj(liczby2)
drukuj(liczby3)

def foo():
    bar()

def bar():
    print("haha")

foo()

a = 3
b = 3

def dodaj_a_b(a , b):
    if a==2:
        return 4
    wynik = a + b
    return wynik

print (dodaj_a_b(10, 20))
wynik = dodaj_a_b(20, 50)
print(wynik)

print (a,b)
print (globals())
print (locals())


def czy_jest_pierwsza(a):
    for i in range(2, a//2 + 1):
        if a % i == 0:
            return False
    return True


assert czy_jest_pierwsza(199)
assert not czy_jest_pierwsza(10)


