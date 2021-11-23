def sum(array):
    sum = 0
    for i in range(0,len(array)):
        sum += array[i]
    return sum
def array2str(array):
    string_ints = [str(int) for int in array]
    string_ints = ','.join(string_ints)
    return string_ints
array = [4,3,7,1,3]
print(sum(array))
print(array2str(array))
print(array)

