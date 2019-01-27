dlugosc=float(input("Długość w cm: "))
szerokosc=float(input("Szerokość w cm: "))
wysokosc=float(input("Wysokość w cm: "))
objetosc=dlugosc*szerokosc*wysokosc

print ("Objętość: ", objetosc, "cm3")
print ("Czy większe od 1 litra: ", objetosc > 1000)

if objetosc > 2000:
    print("Objętość jest większa niż 2 litry")
elif objetosc > 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętośc jest mniejsza niż 1 litr")

print ("To jest już koniec programu")


