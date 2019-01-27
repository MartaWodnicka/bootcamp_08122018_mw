def przytnij(data, start, stop):
    """
    Przycina listę w oparciu o zadane funkcje.
    :param data: list
    :param start: function
    :param stop: function
    :return: list
    """
    out = []
    for el in data:
        if start(el):
            out.append(el)
            if stop(el):
                break
    return out

# print(przytnij([1, 2, 3, 4, 5, 6], start=lambda x: x>3, stop=None))
# print(przytnij(list(range(1000)), start=lambda x: x>100, stop=lambda x: x%11 == 0))

def test_przytnij():
    wynik = przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    )
    assert wynik == [4, 5, 6]


def test_przytnij2():
    wynik = przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 8,
    )
    assert wynik == [4, 5, 6, 7]