class Queue:
	def __init__(self,n):
		self.input = []
		self.interim = []
		self.size = 0
		self.n = n
	def push(self,data):
		self.input.append(data)
		self.size = self.size + 1
	def pop(self):
		x = self.size - self.n
		for i in range(self.n):
			self.interim.append(self.input.pop(0))
		for i in range(self.n):
			self.input.append(self.interim.pop())
		for i in range(x):
			self.input.append(self.input.pop(0))
		return self.input



q = Queue(2)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.push(60)
print q.pop()
