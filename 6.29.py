array1 = [5, 4, 3, 2, 6, 5]
array2 = [4,5,2]
check = ""
for i in range(0, len(array2)):
    if array2[i] in array1:
        check += "a"
    else:
        check += "b"
if check == ("a" * len(array2)):
    print(True)
else:
    print(False)
