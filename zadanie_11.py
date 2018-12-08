x=int(input("Podaj pozycję gracza X: "))
y=int(input("Podaj pozycję gracza Y: "))

if x > 90 and y > 90:
    print("Gracz znajduje się w prawym górnym rogu")
elif x <10 and y > 90:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętośc jest mniejsza niż 1 litr")