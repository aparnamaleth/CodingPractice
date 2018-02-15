class Queue:
	def __init__(self):
		self.input = []
		self.output = []
	def push(self,data):
		self.input.append(data)
	def pop(self):
		if not self.output:
			while self.input:
				self.output.append(self.input.pop())
		return self.output.pop()
	def peek(self):
                if not self.output:
                        while self.input:
				self.output.append(self.input.pop())
		return self.output[-1]


q = Queue()
q.push (10)
q.push(20)
q.pop()	
q.pop()
print q.output	
