text = input("Podaj tekst: ")

# text1 = "Ala ma kota"
# text2 = "Ala <ma> kota"
# text3 = "Ala <>ma kota"

dlugosc = 0
licz = False

for znak in text:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False
        break # opcjonalnie
    elif licz:
        dlugosc += 1

# print(dlugosc)
# assert dlugosc == 0
print(f"liczba znaków pomiędzy <> wynosi {dlugosc}")