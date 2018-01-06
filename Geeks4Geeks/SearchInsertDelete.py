def Search(Arr, key):
	n = len(Arr)
	for i in range (n):
		if Arr[i] == key:
			return True
def Insert(Arr, key):
	Arr.append(key)
def Delete(Arr, key):
	Arr.remove(key)

Arr = [1,2,3,4,5,6,7,8,9]
key = 2
Answer = Search(Arr, key)
print Answer
Insert(Arr, key)
print Arr
Delete(Arr, key)
print Arr
