class Stack:
	def __init__(self):
		self.top = 0
		self.array = []
	def isEmpty(self):
		if len(self.array) == 0:
			return True
		else:
			return False

	def peek(self):
		if (self.isEmpty()):
			return ("Underflow")
		else:
			return self.array.pop()

	def push(self,data):
		self.array.append(data)
		self.top = self.top + 1
		print("Pushing"), self.array

	def pop(self):
		if (self.isEmpty()):
                        return ("Underflow")
		else:
			self.top = self.top - 1
			return self.array.pop()

stack = Stack()
stack.push(10)
stack.push(20)
print stack.pop()


