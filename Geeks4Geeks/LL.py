class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None
	def printlist(self):
		temp = self.head
		while temp:
			print temp.data
			temp = temp.next

LL = Linkedlist()
LL.head = Node(20)
newnode1 = Node (30)
newnode2 = Node (40)
LL.head.next = newnode1
newnode1.next = newnode2
LL.printlist()
