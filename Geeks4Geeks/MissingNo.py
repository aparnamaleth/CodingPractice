def MissingNo(Arr, n):
	total = 0
	a = Arr[0]
	print a
	b = Arr[-1]
	print b
	for i in Arr:
		total = total + i
	actual_total = n/2* (a + b)
	answer = actual_total - total
	print answer

Arr = [1,2,4,5,6]
n = 6
MissingNo(Arr, n) 
