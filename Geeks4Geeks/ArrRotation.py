def ArrayRot(A1, r):
	x = len(A1)
	temp = A1[0]
	for i in range(0,x-1):
		A1[i] = A1[i+1]
	A1[x-1] = temp
	if r == 1:
		return A1
	else:		
		r = r-1
		return ArrayRot(A1,r)

A1 = [1,2,3,4,5]
r = 2
Answer = ArrayRot(A1,r)
print Answer
