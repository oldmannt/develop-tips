class Node:
	def __init__(self, data):
		self.data = data
		self.check = False
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, data):
		if self.front == None:
			self.front = data
		if self.rear == None:
			self.rear = data
		else:
			self.rear.next = data
			self.rear = data

	def pop(self):
		node = self.front
		if self.front != None:
			self.front = node.next
		return node

queue = Queue()
def board_search(graph, data):
	node = graph
	while node:
		if node.data == data: return True
		if node.check != True:
			node.check = True

			bros = node.next
			while bros:
				queue.enqueue(bros)
				bros = bros.next

		node = queue.pop()