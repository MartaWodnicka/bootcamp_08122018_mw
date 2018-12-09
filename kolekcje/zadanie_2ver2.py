dane= input("Podaj liczby, rozdziel je spacjami: ")

dane = dane.split()
dane_2 = []

for d in dane:
    dane_2.append(int(d))

# albo:

# dane=[int(d) for d in dane]

# albo:

dane = map(int,dane)

print (list(dane))
print(dane_2)