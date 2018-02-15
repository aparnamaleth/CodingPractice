class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None
	def push(self,data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode
	def printll(self):
		temp = self.head
		while(temp):
			print temp.data
			temp = temp.next
	def reverse(self):
		
