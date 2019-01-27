liczby = [9, 2, 6, 8, 4, 3, 1, 0]

for i in range(len(liczby)):
    indeks_minimum = i
    for j in range(i, len(liczby)):
        if liczby[j] < liczby[indeks_minimum]:
            indeks_minimum = j
    liczby[i], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[i]

print(liczby)

assert liczby == [0, 1, 2, 3, 4, 6, 8, 9]