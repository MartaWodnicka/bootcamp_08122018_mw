#text = input("Podaj tekst: ")

text = "Ala ma kota aeiouy"
ile_samoglosek = 0
SAMOGLOSKI = 'aeiouy'

for litera in text.lower():
    if litera in SAMOGLOSKI:
        ile_samoglosek += 1

ile_samoglosek2 = 0
for samogloska in SAMOGLOSKI:
    ile_samoglosek2 += text.lower().count(samogloska)

print(ile_samoglosek == 11)
print(ile_samoglosek2 == 11)