def bubblesort(array):
	n = len(array)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if array[j] > array[j + 1] :
				array[j], array[j + 1] = array[j + 1], array[j]

array = [64, 34, 25, 12, 22, 11, 90]

bubblesort(array)

print ("Sorted array is:")
for i in range(len(array)):
	print ("% d" % array[i]),
