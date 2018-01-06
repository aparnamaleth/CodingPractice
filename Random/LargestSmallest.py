def LargestSmallest(Arr, n):
	Arr.sort()
#       If sorting algorithm has to be used then use quicksort
	print("The smallest value is", Arr[0])
	print("The biggest value is", Arr[n-1])


Arr = [2,6,4,9,10,45,32,61]
n = 8
LargestSmallest(Arr, n)

