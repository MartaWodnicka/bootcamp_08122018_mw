import random
gracz_x=random.randint(1, 10)
gracz_y=random.randint (1,10)

skarb_x=random.randint(1, 10)
skarb_y=random.randint (1,10)
print("Położenie gracza: ", gracz_x, gracz_y)
print("Położenie skarbu: ", skarb_x, skarb_y)

odleglosc = abs(gracz_x-skarb_x)+abs(gracz_y-skarb_y)
liczba_krokow = 0

print("Odległość do skarbu: ", odleglosc)
print()

while True:
    print(f"Twoja pozycja to: {gracz_x} {gracz_y}")
    kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo, d-prawo: ")
    if kierunek == "d":
        gracz_x+=1
    if kierunek == "a":
        gracz_x-=1
    if kierunek == "w":
        gracz_y+=1
    if kierunek == "s":
        gracz_y-=1

    liczba_krokow +=1
    odleglosc_2 = abs(gracz_x-skarb_x)+abs(gracz_y-skarb_y)

    if gracz_x < 1 or gracz_y < 1 or gracz_x > 10 or gracz_y > 10:
        print ("Wyszedłeś poza planszę. Koniec gry.")
        break

    if gracz_x==skarb_x and gracz_y==skarb_y:
        print("Wygrałeś!")
        print(f"Odległość wynosiła: {odleglosc}")
        print (f"Zrobiłeś kroków: {liczba_krokow}")
        break

    if odleglosc_2 < odleglosc:
        print ("Ciepło")
    else:
        print ("Zimno")

    if liczba_krokow >= odleglosc *2:
        skarb_x=random.randint(1, 10)
        skarb_y=random.randint (1,10)
        odleglosc = abs(gracz_x-skarb_x)+abs(gracz_y-skarb_y)
        liczba_krokow=0
        print("Przekroczyłeś dozwoloną liczbę ruchów. Skarb zmienił położenie.")
