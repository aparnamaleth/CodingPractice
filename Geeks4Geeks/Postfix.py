class Stack:
	def __init__(self):
		self.top = 0
		self.stack = []
	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False
	def push(self,data):
		self.stack.append(data)
		self.top = self.top + 1
		print "Pushing: ", self.stack
	def pop(self):
		if (self.isEmpty()):
                        return ("Underflow")
		else:
			self.top -= 1
			return self.stack.pop()
	def peek(self):
		if (self.isEmpty()):
                        return ("Underflow")
		else:
			return self.stack[-1]
	def postfix(self, exp):
		for i in exp:
			if (i.isdigit()):
				self.push(i)
			else:
				x = int(self.pop())	
				y = int(self.pop())
				if i == "+":
					self.push(x+y)
				elif i == "-":
					self.push(y-x)
				elif i == "*":
					self.push(y*x)
				else:
					self.push(y/x)
		return self.peek()

exp = "231*+9-"
stack = Stack()
Answer = stack.postfix(exp)
print Answer
			

