def SingleDuplicateNo(Arr, n):
	total = 0
	actualsum = 0
	a = len(Arr)
#	print a
	for i in range (a):
		total = total + Arr[i]
#	print("Total is", total)
	for i in range (1,7):
		actualsum = actualsum + i
#	print actualsum
	missingno = total - actualsum
#	print missingno
	if missingno == 0:
		print("No Duplicate Found")
	else:
		print("The Duplicate number was", missingno)

Arr = [1,2,3,4,5,6,1]
n = 7
SingleDuplicateNo(Arr, n)
