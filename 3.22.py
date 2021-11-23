for i in range(1, 31):
    if i%3 == 0:
        print("trzy")
    elif i%5 == 0:
        print("pięć")
    elif i%15 == 0:
        print("bingo")
    else:
        print(f"{i}")
