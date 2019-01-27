ILE_DNI = 7
temp = 0
i=1
while i<= ILE_DNI:

    komenda = input(f"Podaj temperaturę w dniu {i} lub [k] by zakończyć: ")
    if komenda == 'k':
        break
    temp_i= float(komenda)
    temp += temp_i
    i +=1
print("Średnia temperatura wynosiła: ", temp/i-1)