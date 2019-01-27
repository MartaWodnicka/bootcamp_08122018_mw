print("      ", end="")
for i in range(10):
    print(f"{i:4}", end="")
print()
print()

for wiersz in range(10):
    print (f"{wiersz:4}", end="  ")
    for kolumna in range(10):
        print(f"{wiersz*kolumna:4}", end="")
    print()