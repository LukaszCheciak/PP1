array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

for i in range(len(array1)):
    for n in range(len(array2)):
        if array1[i] == array2[n]:
            break

    if (n == len(array2) - 1):
        print(array1[i], end=" ")