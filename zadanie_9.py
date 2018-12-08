#rok=int(input("Podaj rok urodzenia: "))

#if rok <= 2000:
    #print("Jesteś pełnoletni!")
#else:
   # print("Nie jesteś pełnoletni!")


import datetime

current_year = datetime.datetime.now().year
bd_year = int(input("Podaj rok urodzenia: "))

if current_year -bd_year >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni!")

