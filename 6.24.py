array = [5,1,9,6,1]
suma = 0
liczba = int(input("Podaj liczbę: "))
for i in range(0,len(array)):
    if int(liczba) > int(array[i]):
        suma += 1
    else:
        continue
print(suma)
