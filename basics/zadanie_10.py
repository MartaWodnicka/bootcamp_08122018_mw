liczba_1=float(input("Podaj pierwszą liczbę: "))
liczba_2=float(input("Podaj drugą liczbę: "))
operator=(input("Podaj rodzaj operacji: "))
#
# if operator == "+":
#     print("Wynik: ", (liczba_1 + liczba_2))
# elif operator == "-":
#     print("Wynik :", (liczba_1 - liczba_2))
# elif operator == "*":
#     print("Wynik :", (liczba_1 * liczba_2))
# elif operator == "/":
#     if liczba_2==0:
#         print("Operacja niedozwolona")
#     else:
#         print("Wynik :", (liczba_1 / liczba_2))
# else:
#     print("Operacja nie jest wspierana")

print (eval(f"{liczba_1} {operator} {liczba_2}"))

