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

	def setvalue(self,data):
		value = 0
		if data == "*" or "/":
			value = 2
		else:
			value = i
		return value

	def conversion(self,exp):
		new = ""
		temp = 0
		for i in exp:
			if i.isdigit():
				new = new + str(i)
			else:
				self.setvalue(i)
				if (self.isEmpty()):
					self.push(i)
				else:
					while(self.top!= 0):
						temp = self.pop()
						self.setvalue(temp)
						if self.setvalue(temp) < self.setvalue(i):
							self.push(temp)
							self.push(i)
						else:
							self.push(i)
							self.push(temp)
		while(self.top!=0):
			new = new + str(self.pop())
					
					
		return new
stack = Stack()
exp = "2+3*5"
Answer = stack.conversion(exp)
print Answer
