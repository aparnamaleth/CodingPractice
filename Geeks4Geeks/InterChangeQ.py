class Queue:
	def __init__(self):
		self.input = []
		self.output = []
		self.size = 0
	def push(self,data):
		self.input.append(data)
		self.size = self.size + 1
	def pop(self):
		x = (self.size)
		for i in range(x/2):
			self.output.append(self.input.pop(0))
		for i in range(x/2):
			self.input.append(self.output.pop())
		for i in range(x/2):
			self.input.append(self.input.pop(0))
		for i in range(x/2):
                        self.output.append(self.input.pop(0))
		while self.output:
			self.input.append(self.output.pop())
			self.input.append(self.input.pop(0))
		return self.input


q = Queue()
q.push(20)
q.push(30)
q.push(40)
q.push(50)
print q.pop()

