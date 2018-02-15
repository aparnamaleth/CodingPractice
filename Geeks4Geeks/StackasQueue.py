class Stack:
	def __init__(self,n):
		self.q1 = []
		self.q2 = []
	def push(self, data):
		self.q1.append(data)
		print("pushing",data)
	def pop(self):
		n = len(self.q1)
		for i in range(n):
			for i in range(n-1):
				self.q1.append(self.q1.pop(0))
			self.q2.append(self.q1.pop(0))
		return self.q2

stack = Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)
print stack.pop()

