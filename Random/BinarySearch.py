def BinarySearch(Arr,l,h,key):
	n = len(Arr)
#	l = 0
#	h = n
	mid = (l+h)//2
	if n == 0:
		return False
	elif l >= h:
		if Arr[0] == key:
			return True
	else:
		if  Arr[mid] == key:
			return True
		elif key < Arr[mid]:
			return BinarySearch(Arr, l, mid, key)
		else:
			return BinarySearch(Arr, (mid+1), h, key)			
Arr = [1,2,4,5,9,13,14]
l = 0
h = len(Arr)
key = 15
Ans = BinarySearch(Arr,l,h,key)
print Ans
if Ans == True:
	print("found")
else:
	print("not found")

