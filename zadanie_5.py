Miasto_A =input("Miasto A: ")
Miasto_B=input("Miasto B: ")
Dystans=int(input("Dystans " + Miasto_A + "-" + Miasto_B + ":"))
Cena_paliwa=float(input("Cena paliwa: "))
Spalanie=float(input("Spalanie na 100km: "))
Koszt= (Dystans/100)*Spalanie*Cena_paliwa
print(f"Koszt przejazdu {Miasto_A} - {Miasto_B} to {Koszt} PLN")

