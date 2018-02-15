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

	def nextgreatelement(self, A):
		n = len(A)
		new = []
                for i in range(n):
			if(self.isEmpty()):
				self.push(A[i])
			else:
				x = self.pop()
				while( x < A[i]):
					new.append(A[i])
									
				self.push(x)
			self.push(A[i])
		new.append(-1)
		print self.array
		return new			
A = [13,2,5,12]
stack = Stack()
Answer = stack.nextgreatelement(A)
print Answer

