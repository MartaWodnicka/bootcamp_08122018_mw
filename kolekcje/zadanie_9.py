produkty = {
    "ziemniaki": 1.99,
    'pomidory': 6.99,
    'woda': 1.79,
}
magazyn = {
    "ziemniaki": 10,
    'pomidory': 10,
    'woda': 10,
}

while True:
    rola = input("Czy jesteś [klient]em [k], czy [dostawca][d], [q] by zakończyć? ")
    if rola.lower() in ['klient', 'k']:
        while True:
            print("Nasz sklep oferuje: ")
            for produkt, cena in produkty.items():
                print(f' - {produkt} - {cena:.2f}')
            zakup = input("Co chcesz kupić? [k] by zakończyć: ")
            if zakup.lower() == 'k':
                print("Zapraszamy ponownie")
                break
            if zakup not in produkty:
                print("Nie ma takiego produkty")
                continue
            waga = float(input(f"Ile chcesz kupić - [{zakup}]: "))
            if waga > magazyn[zakup]:
                print()
                print("!! Nie ma tyle w magazynie !!")
                print(f"W magazynie pozostało: {magazyn[zakup]}")
                print()
            else:
                cena = produkty.get(zakup)
                koszt = waga * produkty[zakup]
                print(f"Za [{zakup}] zapłacisz: {koszt:.2f}")
                magazyn[zakup] -= waga

    elif rola.lower() in ['dostawca', 'd']:
        # ścieżka dostawcy
        # dodanie produktu -'d'
        # zmiana ceny - 'z'
        # prosimy o podanie produkty w formacie nazwa ilosc cena
        while True:
            do_dodania = input("Podaj produkt w formacie [nazwa ilosc cena]: ")
            if len(do_dodania.split()) == 3:
                nazwa, ilosc, cena = do_dodania.split()
                try:
                    ilosc = float(ilosc)
                    cena = float(cena)
                    produkty[nazwa] = cena
                    break
                except ValueError:
                    print("Niepoprawna cena lub ilosc")


            else:
                print("Podałeś produkt w niepoprawnym formacie")
        if nazwa in magazyn:
            magazyn[nazwa] = magazyn[nazwa] + ilosc
        else:
            magazyn[nazwa] = ilosc

        magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc

        print("Dziekuję. Produkt Dodany")
    elif rola.lower() == 'q':
        print("Program przestaje działać")
        break