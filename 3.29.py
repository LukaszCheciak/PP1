srednia = 0
liczba = 1
ilosc_cyfr = 0
while liczba != 0:
        liczba = int(input("Liczba: "))
        srednia += liczba
        ilosc_cyfr += 1
print(f"Srednia wynosi {srednia/(ilosc_cyfr - 1)} a suma wynosi {srednia}")