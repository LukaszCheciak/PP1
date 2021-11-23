array = [-15, 8, -31, 47, -2, 19]
min = array[0]
max = array[0]
for i in range(1,len(array)):
    if array[i]>max:
        max = array[i]
    elif array[i]<min:
        min = array[i]
    else:
        pass


print(f"{min}\n{max}")

