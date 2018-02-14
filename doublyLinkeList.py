# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node(object):
    
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None
    
    
a= Node(1)
b= Node(2)
c= Node(3)
d = Node(4)
e= Node(5)

a.nextnode=b
b.prevnode=a
b.nextnode=c
c.prevnode=b
c.nextnode=d
d.prevnode=c
d.nextnode=e
e.prevnode=d

def print_list(Node):
        
        while Node:
            print Node.value
            if Node.nextnode ==None:
                break
            Node=Node.nextnode
            
            

print_list(a)

