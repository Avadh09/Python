class Stack:
	
	def __init__(self,Limit=10):
		self.stk=[]
		self.limit=Limit
		
	def push(self,item):
		if len(self.stk)>10:
			print "underflow!"
		else:
			self.stk.append(item)
			#print self.stk
			
	def pop(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print 'empty stack'
			return 0
		else:
			return self.stk[-1]
			
	def size(self):
		return len(self.stk)

def checkBalance(input):
	check=Stack()
	for symbols in input:
		if symbols in ["(","{","["]:
			check.push(symbols)
			#print check.peek()

		if symbols in [")","}","]"]:
			if check.size()==0:
				return "Error: Unbalanced Expression"
			else:
				#print "here"
				symbol=check.pop()
				#print symbol
				if symbol=="(" and symbols==")":
					continue
				elif symbol=="{" and symbols=="}":
					continue
				elif symbol=="[" and symbols=="]":
					continue
				else:
					return "Unbalanced symbols"

	if check.size()==0:
		print check.peek();
		return "Balanced Expression!!"
	else:
		print check.peek();
		return "Unbalanced symbols"


#s=Stack()
print checkBalance("()[]{{()}}")

#print "check:",check


			

						




