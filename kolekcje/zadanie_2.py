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

