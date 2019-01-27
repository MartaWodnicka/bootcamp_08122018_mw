lista = [100, -100, 2, -2, 100, 2, -2, 0]
licznik_dodatnich = 0
licznik_ujemnych = 0

for liczba in lista:
    if liczba>0:
        licznik_dodatnich +=1
    elif liczba<0:
        licznik_ujemnych +=1

print(f"Liczba dodatnich: {licznik_dodatnich}, Liczba ujemnych {licznik_ujemnych}")

dodatnie = [x for x in lista if x>0]
ujemne = [x for x in lista if x<0]

licznik_dodatnich = len(dodatnie)
licznik_ujemnych = len(ujemne)

print(f"Liczba dodatnich: {licznik_dodatnich}, Liczba ujemnych {licznik_ujemnych}")
