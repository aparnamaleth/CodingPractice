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

	def balancebrak(self, exp):
		balanced = 0
		for i in exp:
			if i in ["(", "{", "["]:
				self.push(i)
			else:
				if i == ")" and self.peek == "(":
					self.pop()
					balanced = 0
				elif i == "]" and self.peek == "[":
					self.pop()
					balanced = 0
				elif i == "}" and self.peek == "{":
					self.pop()
					balanced = 0
				else:
					balanced = 1
		
		print self.array
		if balanced == 0:
			return True
		else:
			return False

exp = "[{(()}]"
stack = Stack()
Answer = stack.balancebrak(exp)
print Answer
