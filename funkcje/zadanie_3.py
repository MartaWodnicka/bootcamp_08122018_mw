def policz_znaki(napis, start="<", stop=">"):
    wynik=0
    poziom = 0

    for znak in napis:
        if znak == start:
            poziom += 1
        elif znak == stop:
            poziom -= 1
        elif poziom:
            wynik += poziom

    return wynik

def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0

def test_policz_znaki_w_niepustym_napisie_bez_nawiasow():
    assert policz_znaki("ala ma kota") == 0

def test_policz_znaki_pierwszy_poziom():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <kota a> kot ma ale') == 6

def test_policz_znaki_1_poziom_ale_nawiasy_kilka_razy():
    assert policz_znaki('ala ma <kota> a kot <ma> ale') == 6

def test_policz_znaki_1_poziom_inne_nawiasy():
    assert policz_znaki('ala ma [kota] a <kot> [ma] ale', '[', ']' ) == 6

def test_policz_znaki_2_poziomy_zagnieżdzenia():
    assert policz_znaki('ala ma <<kota>> a kot <ma> ale') == 10