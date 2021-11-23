def fun(array):
    array1 = str()
    for i in range(0, len(array)):
        if i != len(array)-1:
            array1 += str(array[i])+","
        else:
            array1 += str(array[i])
    return (array1)
print(fun([5,4,3,2,6,5]))
