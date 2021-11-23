dlugosc = int(input("Podaj dlugosc prostokata: "))
wysokosc = int(input("Podaj wyskosc prostokata: "))
print("* "*dlugosc)
for i in range(wysokosc - 2):
        print("*" + " " * (2*dlugosc-3) + "*")
print("* "* dlugosc)
