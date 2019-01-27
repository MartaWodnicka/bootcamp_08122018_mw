
# liste zawierajaca liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1

print([x/10 for x in range(11)])
# I zbiór tupli zawierajacych 3 elementy - dana liczbe, jej kwadrat i jej szescian - w przedziale od -10 do 10

print({(x, x**2, x**3) for x in range(-10, 11)})

# I słownik mapujacy napisy na ich długosc powstały ze zbioru napisów
napisy = {"Ala ma kota", "kot ma alę", "Zażółć gęślą jaźń"}

print({x: len(x) for x in napisy})