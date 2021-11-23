file = open("numbers.txt", "r")
suma = 0
for i in file:
    suma += int(i)
file.close()
print(suma)
