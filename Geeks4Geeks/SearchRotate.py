def SearchRotArr(Arr, s, b, key):
	if s>b:
		print("No")
		return 1
        mid = s+b//2
        if Arr[mid] == key:
        	print("Middle element match") 
		return 1      
        if Arr[s] <= Arr[mid]: 
		if Arr[s] <= key and Arr[mid] >= key:
                       return SearchRotArr(Arr, s, mid-1, key)
		return SearchRotArr(Arr, mid+1, b, key)
        if Arr[b] >= key and Arr[mid] <= key:
		return SearchRotArr(Arr, mid+1, b, key)
	else:
		return SearchRotArr(Arr, s, mid-1, key)
Arr = [3,4,5,1,2]
key = 3
a = SearchRotArr(Arr, 0, len(Arr), key)
print a


