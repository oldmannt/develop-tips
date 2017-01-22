
def swap(a, x, y):
	#print "swap {0},{1}".format(x,y)
	t = a[x]
	a[x] = a[y]
	a[y] = t

def part(a, l, r):
	i = l
	#print "{0}, {1}".format(l, r-1)
	for x in xrange(l,r):
		#print "x = {0}".format(x)
		if a[x]<=a[r]:
			swap(a,x,i)
			i += 1
	swap(a,r,i)
	return i

def quickSort(a, s, e):
	if s>= e: return
	i = part(a,s,e)
	quickSort(a, s, i-1)
	quickSort(a, i+1, e)

import random

a = [4,23,5,6,74,34,67,32,5,6,45,7,2,1,9]
s = a#[5,2,3,4]
#for x in xrange(1,10):
#	a.append(random.randint(0, 10))

print s
quickSort(a, 0, len(a)-1)
#i = part(s, 0, len(s)-1)
print s