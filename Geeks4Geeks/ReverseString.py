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
                        self.top = self.top - 1
                        return self.stack.pop()
        def peek(self):
                if (self.isEmpty()):
                        return ("Underflow")
                else:
                        return self.stack[-1]
	def reversestr(self, answer):
		for i in answer:
			self.push(i)
		print self.stack
		answer = ""
		while(self.top != 0):
			a = self.pop()
			answer = answer + a
		return answer

answer = "Aparna"
stack = Stack()
X = stack.reversestr(answer)
print X
