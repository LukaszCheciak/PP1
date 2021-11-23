pin = 2137
proba = 3
while proba > 0:
    in_pin = int(input("wprowadź pin "))
    if pin == in_pin:
        print("prawidłowy pin")
    else:
        proba -= 1
        print("Nieprawidłowy pin, spróbuj jeszce raz")
print("Karta zablokowana")
