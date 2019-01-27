# przyklady input

#x=int(input("Podaj wartość x: "))
#y=int(input("Podaj wartość y: "))

#print("Suma:",x+y)

# przykłady wartości logiczne

# operatory porównania
# ==, <, >, <=, >=, !=

# przykłady spójników
# and, or, not

# x=2
# y=5
#
# print (x>1 and y>1)
# print (x>1 or y>1)

# i=0
# while True:
#     if i==5:
#         i+=1
#         continue
#     print (i)
#     i += 1 #i=i+1
#     if i == 100:
#         break
#
# i=0
# while i<10:
#     komenda= input("Podaj komendą: ")
#     if komenda =="koniec":
#         break
#     if komenda =="dodaj":
#         a=int(input("Podaj a:"))
#         b=int(input("Podaj b:"))
#         print (a+b)

# NAPISY

tekst ="Ala ma kota"
#        #012345678910
#
# print (tekst[0])
# print (tekst [2:])
# print (tekst [:5])
# print (tekst [-1])
# print (tekst [-6])
# print (tekst [::2])
#
# i=0
# while i<len(tekst):
#     print(tekst[i])
#     i+=1
#
# #łatwiej:
#
# for litera in tekst:
#     print(litera)
#
# for i, litera in enumerate(tekst):
#     print(i,litera)

krotka = (1,2,3,1,1)
print(type(krotka))
print(krotka)
print(krotka[0])

for el in krotka:
    print(el)

print(dir(krotka))
print (krotka.count(1))

krotka_2 = ("Napis 1", "Napis 2", "Napis 1",1,2,3)
print(krotka_2.index("Napis 1"))
print(krotka_2.count("Napis 1"))

