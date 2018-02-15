class Queue:
	def __init__(self):
		self.queuearray = []
		self.stackarray = []
	def push(self,data):
		self.queuearray.append(data)
		print("Pushing"), data
	def pop(self):
		if not self.stackarray:
			while self.queuearray:
				self.stackarray.append(self.queuearray.pop(0))
			while self.stackarray:
				self.queuearray.append(self.stackarray.pop())	
		return self.queuearray
	

q = Queue()
q.push("a")
q.push("b")
q.push("c")

print q.pop()
