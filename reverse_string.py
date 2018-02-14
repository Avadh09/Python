# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:51:21 2018

@author: avadh

Reverse a string using recursion

"""


def reverse(s):
    
    # Base Case
    
    if len(s) == 1:
        return s
    
    return reverse(s[1:]) + s[0]

print reverse("avadh")
    