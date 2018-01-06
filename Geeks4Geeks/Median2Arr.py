def Median2Arr(A1, A2,):
	n = len(A1)
	if n == 2:
		Answer = max(A1[0], A2[0])
		Answer1 = min(A1[1], A2[1])
		Answer = (Answer + Answer1)/2
		return Answer

	if n%2 ==0:
		Med1 = (A1[n/2] + A1[n/2 + 1]) / 2
		Med2 = (A2[n/2] + A2[n/2 + 1]) /2
	else:
		Med1 = A1[n/2]
		Med2 = A2[n/2]

	if Med1 == Med2:
		return Med1

	elif	Med1 > Med2:
		A1 = A1[:n/2+1]
		A2 = A2[n/2: ]
		return Median2Arr(A1, A2)
	else:
                A1 = A1[n/2:]
                A2 = A2[:n/2+1]
                return Median2Arr(A1, A2)

A1 = [1,2,3,6]
A2 = [4,6,8,10]

Answer = Median2Arr(A1, A2)
print Answer
