import random
def rand_elem(array):
    a = array[random.randint(0,len(array))]
    return a
print(rand_elem([4,2,8,4,7,9,5]))