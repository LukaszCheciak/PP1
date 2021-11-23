array = [15, 8, 31, 47, 2, 19]
parzyste = 0
nieparzyste = 0
for i in range(0,len(array)):
    if array[i]%2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f"parzystych jest {parzyste}\nnieparzystych jest {nieparzyste}")