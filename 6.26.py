array = [1,4,2,7,4,7,9,5]
array_odd = []
array_even = []
array1 = []
for i in range(0,len(array)):
    if array[i]%2 == 1 :
        array_odd += str(array[i])
    else:
        array_even += str(array[i])
array1 = array_even
array1 += array_odd
print(array1)