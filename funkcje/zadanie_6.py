def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            for el in splaszcz(element):
                out.append(el)
        else:
            out.append(element)
    return out


def test_splaszcz_pusta_lista():
    assert splaszcz([]) == []

def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_spalszcz_zagniezdzona_lista():
    assert splaszcz([1, 2, [3, 4]]) == [1, 2, 3, 4]
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]