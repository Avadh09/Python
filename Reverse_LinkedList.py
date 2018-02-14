# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:37:28 2018

@author: avadh

Linked Lise Reversel
"""

class Node(object):
    
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        #self.prevnode=None

def revese(head):
    
    current= head
    prev =None
    next= None
    
    while current:
        
        next = current.nextnode
        current.nextnode =prev
        prev = current
        
        current = next
        
    return prev




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


print a.nextnode.value
print b.nextnode.value
print c.nextnode.value
print d.nextnode.value

print revese(a)

print e.nextnode.value
print d.nextnode.value
print c.nextnode.value
print b.nextnode.value
