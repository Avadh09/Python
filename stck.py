class Stack:
	
	def __init__(self,Limit=10):
		self.stk=[]
		self.limit=Limit
		
	def push(self,item):
		if len(self.stk)>10:
			print "underflow!"
		else:
			self.stk.append(item)
			print self.stk
			
	def pop(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print 'Stack Undcrflow'
			return 0
		else:
			return self.stk[-1]
			
	def size(self):
		return len(self.stk)
#stk=[]
our_stack = Stack()
our_stack.push("1")
our_stack.push("2")
our_stack.push("14")
our_stack.push("3 ")
our_stack.push("19")
our_stack.push("3")
our_stack. push("99")
our_stack.push("9")
print our_stack.peek()
print our_stack.pop()
print our_stack.peek()
print our_stack.pop()	