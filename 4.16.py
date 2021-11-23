def month(n):
    if n == int(1):
        print("Styczeń")
    elif n == 2:
        print("Luty")
    elif n == 3:
        print("Marzec")
    elif n == 4:
        print("Kwiecień")
    elif n == 5:
        print("Maj")
    elif n == 6:
        print("Czerwiec")
    elif n == 7:
        print("Lipiec")
    elif n ==8:
        print("Sierpień")
    elif n == 9:
        print("Wrzesień")
    elif n==10:
        print("październik")
    elif n == 11:
        print("listopad")
    elif n == 12:
        print("grudzień")
    else:
        print("nie ma takiego miesiąca")
    return n

month(13)