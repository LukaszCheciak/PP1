file = open("products.txt", "a")
file.write(input("Podaj produkt: ")+"\n")
file.close()
file = open("products.txt","r")
print(file.read())
