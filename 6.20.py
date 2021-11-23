def occurs(number,array):
    if number in array:
        return True
    else:
        return False

array = [15,38,7,23,14]
number = int(input("Podaj liczbę: "))

print(occurs(number,array))