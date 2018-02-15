class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class Linkedlist:
	def __init__(self):
		self.head = None
	def insert(self,data):
		newnode = Node(data)
		temp = self.head
		newnode.next = temp
		self.head = newnode
	def insertbehind(self,data):
		temp = Node(data)
		newnode = self.head
		while(newnode):
			if newnode.next == None:
				newnode.next = temp
			newnode = newnode.next
	def delete(self,key):
		newnode = self.head 
		if (newnode):
			if newnode.data == key:
				self.head = newnode.next				
		while(newnode):
			if newnode.data == key:
				break	
			prev = newnode
			newnode = newnode.next
		prev.next = newnode.next
		newnode = None		
	def deletepos(self,pos):
		newnode = self.head
		if (pos == 0):
			self.head = newnode.next
			return
		else:
			for i in range(0, pos-1):
				newnode = newnode.next
			prev = newnode
			count = 1
			while(newnode):
				if (pos == count):
					break
				count = count + 1
				newnode = newnode.next
			if newnode.next is None:
				return
			else:
				prev.next = newnode.next
				return
		newnode = None
	
	def printelements(self):
		newnode = self.head 
		while(newnode):
			print newnode.data
			newnode = newnode.next
ll = Linkedlist()
ll.insert(40)
ll.insert(30)
ll.insert(20)
ll.insert(10)
ll.printelements()
ll.deletepos(3)
ll.printelements()
