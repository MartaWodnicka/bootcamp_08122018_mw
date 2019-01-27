def wiecej_niz(napis, prog):
    # wynik = set()
    # unikalne = set(napis)
    # for c in unikalne:
    #     if napis.count(c) > prog:
    #         wynik.add(c)
    # return wynik

    return {x for x in set(napis) if napis.count(x) > prog}


def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}
    assert wiecej_niz('aaaa bbbb ccc', 3) == {'a', 'b'}

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('', 3) == set()