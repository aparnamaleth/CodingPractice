#def SortByFreq(A):
#	new = sorted(A, key = A.count, reverse = False)
#	print new
#A = [2,3,2,4,5,3,3,4]
#SortByFreq(A)	

def SortByFreq(A):
	mydict = {}
	new = []
	for i in A:
		if i in mydict.keys():
			mydict[i] += 1
		else:
			mydict[i] = 1
	for i in mydict:
		mydict[i] > mydict[i+1]
		


freqdict = [2,3,2,4,5,3,3,4]
sortFreqDict

