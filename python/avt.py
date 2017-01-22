class CircleQueue:
	def __init__(self, size):
		self.buf = [-1]*size
		self.front = 0
		self.rear = 0

	def enqueue(self,data):
		if self.full():
			print "enqueue full"
			return
		self.buf[self.rear] = data
		self.rear = (self.rear+1)%len(self.buf)
		#print "enqueue.rear {0}".format(self.rear)

	def empty(self):
		#print "queue size:{0}".format(self.size())
		return self.front == self.rear

	def full(self):
		return (self.rear+1)%len(self.buf) == self.front

	def get(self):
		return self.buf[self.front]

	def pop(self):
		rt = self.buf[self.front]
		self.buf[self.front] = -1
		self.front = (self.front+1)%len(self.buf)
		return rt

	def size(self):
		return (self.rear-self.front+len(self.buf))%len(self.buf)

class AVTNode:
	def __init__(self, data):
		self.data = data
		self.l = None
		self.r = None
		self.h = 0

def getstrB(node):
	queue = CircleQueue(20)
	queue.enqueue(node)
	str = ""
	while not queue.empty():
		n = queue.pop()
		if n == None:
			str += "-1,"
			continue
		else:	
			#print "while n:{0}".format(n.data)
			str += "{0},".format(n.data)
		queue.enqueue(n.l)
		queue.enqueue(n.r)
	return str

def right(node):
	if node.r == None:
		return node
	return right(node.r)

def left(node):
	if node.l == None:
		return node
	return left(node.l)

def height(node):
	if node == None: return 0
	elif node.h != 0: return node.h
	lh = height(node.l)
	rh = height(node.r)
	return (lh if lh >= rh else rh)+1

def getstr(node):
	if node == None: return ""
	return getstr(node.l) + "{0},".format(node.data) + getstr(node.r)

def rotateLL(node):
	top = node.l
	node.l = top.r
	top.r = node
	node.h = max(height(node.l),height(node.r))+1
	top.h = max(height(top.l),node.h)+1
	return top

def rotateRR(node):
	top = node.r
	node.r = top.l
	top.l = node
	node.h = max(height(node.l),height(node.r))+1
	top.h = max(height(top.l),node.h)+1
	return top

def rotateLR(node):
	node.l = rotateRR(node.l)
	return rotateLL(node)

def rotateRL(node):
	node.r = rotateLL(node.r)
	return rotateRR(node)

def add(node, data):
	if node == None:
		#print "add new {0}".format(data)
		node = AVTNode(data)
	elif data <= node.data:
		#print "node:{0} add l {1}".format(node.data,data)
		node.l = add(node.l, data)
		if height(node.l)-height(node.r)==2:
			if data <= node.l.data:
				node = rotateLL(node)
			else:
				node = rotateLR(node)
	elif data > node.data:
		#print "node:{0} add r {1}".format(node.data,data)
		node.r = add(node.r, data)
		if height(node.r)-height(node.l)==2:
			if data <= node.r.data:
				node = rotateRL(node)
			else:
				node = rotateRR(node)
	node.height = max(height(node.l),height(node.r))+1
	return node

def size(node):
	if node == None : return 0
	return size(node.l)+size(node.r)+1

def remove(node, data):
	return node

def search(node, data):
	if node == None: return None
	if node.data == data: return node
	if search(node.l) == None:
		search(node.r)

ls = [1,6,2,5,8,7,9,10]
avt = AVTNode(3)
for x in ls[0:]:
	add(avt,x)
print getstr(avt)
print getstrB(avt)