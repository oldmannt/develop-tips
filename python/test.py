
def revers_str(str):
	if len(str) == 1:
		return "e"
	else:
		sub = str[1:]
		sub_rt = revers_str(sub)
		return sub_rt + str[0]

def binery_search(array, size, value):
	l = 0
	u = size - 1
	
	i=0
	while l<u:
		m = (u+l)/2
		if array[m] == value:
			return m
		if value > array[m]:
			l = m+1
		else:
			u = m-1
		print "{0} {1} {2}".format(m, l, u)
	if array[l] == value:
		return l
	return -1

#print revers_str('fire')

#a1 = []
#for x in xrange(100):	a1.append(x)
#print binery_search(a1,len(a1),99)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class List:
	def __init__(self):
		self.head = Node(None)
		self.tail = self.head

	def push(self,data):
		tmp = Node(data)
		if self.head.data == None:
			self.head = tmp
		self.tail.next = tmp
		self.tail = tmp

	def search(self,data):
		it = self.head
		while it != None:
			if it.data == data:
				return True
			it = it.next
		return False

	def remove(self,data):
		it = self.head
		if it.data == data:
			self.head = it.next
		while it.next != None:
			if it.next.data == data:
				it.next = it.next.next
			it = it.next

	def output(self):
		str = ""
		it = self.head
		while it != None:
			str += "{0},".format(it.data)
			it = it.next
		print str

#ls = List()
#for x in xrange(10):	
#	ls.push(x)
#	ls.output()
#ls.output()
#ls.remove(5)
#print ls.search(5)

class CircleQueue:
	def __init__(self, size):
		self.front = 0
		self.rear = 0
		self.buffer = [-1]*size

	def size(self):
		return (self.rear - self.front + len(self.buffer))%len(self.buffer)

	def enqueue(self, data):
		self.buffer[self.rear] = data
		self.rear = (self.rear+1)%len(self.buffer)

	def get(self):
		return self.buffer[self.front];

	def pop(self):
		data = self.get()
		self.buffer[self.front] = -1
		self.front = (self.front+1)%len(self.buffer)
		return data

	def show(self):
		str = ""
		i = self.front
		while i != self.rear:
			str += "{0},".format(self.buffer[i])
			i = (i+1)%len(self.buffer)
		print str
		str = "front:{0} rear:{1} len:{2} ".format(self.front, self.rear, self.size())
		for x in self.buffer:
			str += "{0}".format(x)
		print str

#cq = CircleQueue(10)
#for x in xrange(10):
#	cq.enqueue(x)
#cq.show()
#for x in xrange(5):
#	print cq.pop()
#cq.show()
#cq.enqueue(3)
#cq.show()

class BTNode:
	def __init__(self, data):
		self.data = data
		self.l = None
		self.r = None
		self.h = 0

	def right(self):
		if self.r == None:
			return self
		if self.r != None: return self.r.right()

	def left(self):
		if self.l == None:
			return self
		if self.l != None: return self.l.left()

	def height(self):
		h = 0
		if self.l != None: h += l.height()
		if self.r != None: h += r.height()
		return h

	def getstr(self):
		rt = ""
		if self == None: return ""
		if self.l != None: 
			rt += self.l.getstr()

		rt += "{0},".format(self.data)

		if self.r != None: 
			rt += self.r.getstr()
		return rt

	def add(self, data):
		if data <= self.data:
			if self.l == None : self.l = BTNode(data)
			else: self.l.add(data)
		if data > self.data:
			if self.r == None : self.r = BTNode(data)
			else: self.r.add(data)

	def size(self):
		rt = 1
		if self.l != None: rt += self.l.size()
		if self.r != None: rt += self.r.size()
		return rt

	def remove(self, data):
		#print "remove {0}, self:{1}".format(data, self.data)
		if self.data > data:
			if self.r == None: return self
			self.r = self.l.remove(data)
		if self.data < data:
			self.r = self.r.remove(data)
		if self.data == data:
			#print "remove == data {0}".format(data)
			if self.l != None and self.r != None:
				#print data
				self.data = self.l.right().data
				self.l = self.l.remove(self.data)
			elif self.l != None:
				self = self.l
			else:
				self = self.r
		return self

	def search(self, data):
		if self.data == data: return self
		if self.l != None and self.l.search(data):
			return self
		if self.r != None and self.r.search(data):
			return self
		return None

ls = [2,6,1,3,5,8,0,7,9]
bt = BTNode(4);

for x in ls:
	bt.add(x)
print "size: {0}".format(bt.size())
print bt.getstr()
print "search 3: {0}".format(bt.search(8))
print "search 10: {0}".format(bt.search(10))
bt.remove(4)
print bt.getstr()
print bt.data

class AVTNode(BTNode):
	def __init__(self, data):
		super().__init__(data)

	def add(self, data):
		if data <= self.data:
			lh = 0
			if self.l == None:
				self.l = AVTNode(data)
				lh = 1
			else:
				self.l.add(data)
				lh = self.l.height()

		

