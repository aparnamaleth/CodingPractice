class Node:
	def __init__(self, data):	
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode

	def pop(self, position):
		temp = self.head
		if position == 0:
			self.head = temp.next
			temp = None
			return
		else:
			for i in range(position-1):
				temp = temp.next
				if temp is None:
					break
			if temp is None:
				return
			if temp.next is None:
				return
			next = temp.next.next
			temp.next = None
			temp.next = next
	def printll(self):
		temp = self.head
		while(temp):
			print temp.data
			temp = temp.next




ll = LinkedList()
ll.push(20)
ll.push(30)
ll.push(40)
ll.pop(2)
ll.printll()		

