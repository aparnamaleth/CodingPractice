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

	def pop(self,key):
		temp = self.head
		if temp != None:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return ("Deleted at head")
		while(temp):
			if temp.data == key:
				break
			prev = temp
			temp = prev.next
		
		if temp==None:
			return
		
		prev.next = temp.next
		temp = None
        def printlist(self):
                temp = self.head
                while temp:
                        print temp.data
                        temp = temp.next

ll = Linkedlist()
ll.push(2)
ll.push(3)
ll.push(4)
ll.printlist()
ll.pop(5)
ll.printlist()
