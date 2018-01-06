def MajorityElement(Arr):
	n = len(Arr)
	x = n/2 + 1
	my_dict = {}
	for i in Arr:
		if i in my_dict.keys():
			my_dict[i] = my_dict[i] + 1
			if my_dict[i] >= x:
				print("The answer is", i) 
		else:
			my_dict[i] = 1
	print my_dict	
Arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
MajorityElement(Arr)

