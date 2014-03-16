import pdb

class Node(object):

	head = None
	size = 0
	def __init__(self):
		self.data = None
		self.index = None
		self.next = None
	
	def add(self,index,data):
		self.size = self.size + 1
		node = Node()
		node.data = data
		node.index = index
		if self.head == None:
			self.head = node
			return
		curr = self.head
		prev =curr
		while(curr != None):
			if(curr.data <= data):
				prev = curr
				curr = curr.next
			else:
				break
		prev.next = node
		node.next = curr
		return

	def display(self):
		if self.head == None:
			return
		curr = self.head
		while(curr!= None):
			print curr.index," ",curr.data
			curr = curr.next
		return

	def update(self,index,data):
		if self.head == None:
			return False
		curr = self.head
		while(curr!=None and curr.index != index):
			curr = curr.next
		if curr!= None:
			curr.data = data
			return True
		else:
			return False

	def getsize(self):
		return self.size
	def sorting(index):
		
		print "index is ", index
		if index > 1:
			mid = index//2
			left= mid
			right=mid+1
			sorting(left)
			sorting(right)
		
			i,j,k = 0
			while i<left and j<right:
				iValue = alist(i)
				jValue = alist(j)
				if iValue < jValue:
					changeValue(k,iValue)
					i +=1
				else:
					changeValue(k,jValue)
					j += 1
				k += 1
		
			while i < left:
				iValue = alist(i)
				changeValue(k,iValue)
				i ,k +=1
			while j < right:
				jValue = alist(j)
				changeValue(k,jValue)
				j,k += 1
			
		return
	
	def changeValue(index,data):
		if self.head == None or index > self.size:
			return
		
		curr = self.root	
		while(curr != None and count <= index):
			count ++
			curr = curr.next
		curr.data = data

print "We are about to create list"
one = Node()
#pdb.set_trace()
one.add(0,10)
one.add(1,30)
one.add(4,50)
one.add(2,20)
one.add(3,40)
one.display()
one.update(4,10)
one.update(2,60)
one.display()
print "size is ",one.getsize()

				
				
