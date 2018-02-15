class StackNode:
	def __init__(self,data):
		self.data = data
		self.root = None

class Stack:
	def __init__(self):
		self.root = None

	def isEmpty(self):
		if self.root is None:
			return True
		else:
			return False

	def top(self):
		if(isEmpty()):
			return float("-inf")
		else:
			return self.root.data

	def pop(self):
		if(self.isEmpty()):
                        return float("-inf")
		else:
			temp = self.root
			self.root.next = self.root
			popped = temp.data
			return popped

	def push(self,data):
		newnode = StackNode(data)
		newnode.next =  self.root
		self.root = newnode
		print("Added")
						 
				 	
	


stack = Stack()
stack.push(10)
stack.push(20)
stack.pop()
print stack


