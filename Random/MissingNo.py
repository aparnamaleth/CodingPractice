def MissingNoInTheRange(Arr, n):
	total = 0
	a = len(Arr)
	for i in range (a):
		total = total + Arr[i]
	actualsum = n/2*(11)
	missingno = actualsum - total
	print missingno
	if missingno == 0:
		print("No number was missing")
	else:
		print("The missing number was", missingno)

Arr = [1,2,3,5,6,7,8,9,10]
n = 10
MissingNoInTheRange(Arr, n)

