liczby = [5,2,1,4,3]


temp=liczby[0]
liczby[0]=liczby[2]
liczby[2]=temp
print(liczby)

assert liczby==[1,2,5,4,3]

liczby[0], liczby[2] = liczby[2], liczby[0]

for el in liczby:
    pass

for i in range(len(liczby)):
    liczby[i]