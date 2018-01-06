def SequentialSearch(Arr, n, key):
        for i in range (n):
        	if Arr[i] == key:
			a = 1
			b = i + 1
	if a == 1:
		print("Element found at", b)
	else:
		print("No element found")

Arr = [1,9,2,8,7,3,4,5,6]
n = 9
key = 3
SequentialSearch(Arr, n, key)

