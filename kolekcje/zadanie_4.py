licznik = 0
for liczba in range (0, 101):
    if liczba%3==0 or liczba%5==0:
        print(liczba)
        licznik +=1

print(f"W przedziale 0-100 jest {licznik} liczb podzielnych przez 3 lub 5")