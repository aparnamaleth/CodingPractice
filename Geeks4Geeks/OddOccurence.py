def OddOccurence(Arr):
	n = len(Arr)
	d = {}
	for i in Arr:
		if i in d.keys():
			d[i] = d[i] + 1
		else:
			d[i] = 1
	for i in d.keys():
		if d[i]%2 !=0:
			print i 

def OddOccur(Arr):
	total = 0
	for i in Arr:
		total = total ^ i
	print total
Arr = [2, 2, 3, 3, 3, 4, 4]
OddOccurence(Arr)
OddOccur(Arr)
