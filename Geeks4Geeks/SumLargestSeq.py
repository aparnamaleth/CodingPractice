def SumLargestSeq(Arr):
	max_sofar = Arr[0]
	current_max = Arr[0]
	for i in Arr:
		current_max = max (i, current_max + i)
		max_sofar = max (max_sofar, current_max)
	print max_sofar
Arr = [ -2, -3 , 4, -1 -2, 1, 5, -3]
SumLargestSeq(Arr)
