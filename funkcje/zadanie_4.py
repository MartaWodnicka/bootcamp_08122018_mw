def formatuj(*napisy, **zmienne):
    napis = "\n".join(napisy)
    for zmienna in zmienne:
        napis = napis.replace(f"${zmienna}", zmienne[zmienna])
    return napis


def test_formatuj_napis_bez_znacznikow():
    assert formatuj("Hello World!") == "Hello World!"


def test_formatuj_wiele_napisow_bez_znacznikow():
    assert formatuj("Hello World!", "Hi Python!") == "Hello World!\nHi Python!"


def test_formatuj_napis_bez_znacznikow_ale_ze_zmienna_jako_argument():
    assert formatuj("Hello World!", name="John") == "Hello World!"


def test_formatuj_napis_bez_znacznikow_ale_ze_zmiennymi_jako_argument():
    assert formatuj("Hello World!", name="John", lastname="Kovalsky") == "Hello World!"


def test_formatuj_napis_ze_zmienna():
    assert formatuj("Hello $name", name="John") == "Hello John"
    assert formatuj("Hello $name $lastname!", name="John", lastname="Kovalsky") == "Hello John Kovalsky!"