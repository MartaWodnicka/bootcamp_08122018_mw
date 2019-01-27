liczby = [1, 2, 3, 4]
liczby2 = [5, 6, 7, 8]
liczby3 = [9, 16, 17, 18]

for i, l in enumerate(liczby):
    print(f'Pozycja={i}, wartość={l}')

for i, l in enumerate(liczby2):
    print(f'Pozycja={i}, wartość={l}')

for i, l in enumerate(liczby3):
    print(f'Indeks={i}, wartość={l}')


def drukuj(lista):
    for i, l in enumerate(lista):
        print(f'Pozycja={i}, wartość={l}')


drukuj(liczby)
drukuj(liczby2)
drukuj(liczby3)


def foo():
    bar()

def bar():
    print("haha")

foo()
bar()
print(bar())

a = 3
b = 3

def dodaj_a_b(a, b):
    if a == 2:
        return 4
    wynik = a + b
    print(globals())
    print(locals())
    return wynik


print(dodaj_a_b(10, 20))
wynik = dodaj_a_b(20, 50)
print(wynik)

print(a, b)
print(globals())
print(locals())

print(foo)

def potega(podstawa, wykladnik=2):
    return podstawa ** wykladnik

print(potega(4))
print(potega(4, 2))
print(potega(4, 3))


def foo(a, b, c, d=1, e=2):
    print(a, b, c, d, e)

foo(1, 2, 3)
foo(1, 2, 3, 3)
foo(1, 2, 3, 3, 2)

# złe
# foo(1, 2, 3, 3, 2, 6)
# foo(1, 2)

foo(c=40, b=20, a=30, d=50, e=70 )


def wykonaj_operacje(operacja, *args):
    print(args)
    print(type(args))
    return operacja(args)


# print(zsumuj('a', 'b', [10, 20]))

print(wykonaj_operacje(min, 10, 20, 20))
print(wykonaj_operacje(sum, 10, 20, 20, 30))
print(wykonaj_operacje(max, 10, 20, 20, 30, 50))

def napisy(*args, **kwargs):
    """
    Napisz funkcję, która przyjmie dowolną liczbę napisów,
    1. Zwróci te napisy połączone znakiem nowej linii
    >>> napisy("a", "b")
    a
    b
    >>> napisy("a", "b", "d")
    a
    b
    d
    """
    tekst = "\n".join(args)

    print(kwargs)
    for k in kwargs:
        tekst = kwargs[k](tekst)

    return tekst

print("-"*40)
print(napisy("a", "b"))

print("-"*40)
print(napisy("a", "b", "c", "d"))


def upper(napis):
    return napis.upper()

def powiel(napis):
    return f'{napis}\n'*2

print("-"*40)
print(napisy("ala", "banan", "celina", "dom", funkcja=powiel, funkcja2=str.title))


def hi():
    return "Hi!"

def goodmorning():
    return "Good Morning"

def przywitaj_sie(greeting_function):
    print(greeting_function())

przywitaj_sie(hi)
przywitaj_sie(goodmorning)



def sprawdz_czy(x, funcja1, funkcja2):
    return funcja1(x) and funkcja2(x)


def sprawdz_czy_podzielna_przez_2_i_3(x):
    return x%2 == 0 and x%3 == 0

print(sprawdz_czy(12, sprawdz_czy_podzielna_przez_2_i_3, lambda x: x > 5, ))