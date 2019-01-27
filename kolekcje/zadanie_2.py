#Wersja 1:

liczby =[]
i=0
while i<10:
    liczba=input("Podaj liczbę lub k aby zakończyć: ")
    if liczba == 'k':
        break
    liczba= int(liczba)
    liczby.append(liczba)
    i+=1

print("Średnia wynosi: ", sum(liczby)/len(liczby))


#Wersja 2:

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