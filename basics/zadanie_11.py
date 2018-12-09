x=int(input("Podaj pozycję gracza X: "))
y=int(input("Podaj pozycję gracza Y: "))

if 100 >= x >= 90 and 100 >= y >= 90:
    print("Gracz znajduje się w prawym górnym rogu")
elif 0 <= x >= 10 and 100 >= y >= 90:
    print("Gracz znajduje się w lewym górnym rogu")
elif 0 <= x <= 10 and 0 <= y <=10:
    print("Gracz znajduje się w lewym dolnym rogu")
elif 100 >= x >= 90 and 0 <= y <= 10:
    print("Gracz znajduje się w prawym dolnym rogu")
elif 0 < x < 100 or 0 < y < 100:
    print("Gracz znajduje się poza planszą")
else:
    print("Gracz znajduje się w centrum")


