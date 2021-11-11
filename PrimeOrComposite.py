# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 21:09:48 2021

@author: ledin
"""
import math

num = int(input("Enter an integer: "))


if num == 0 or num == 1 or num == -1:
    print("Your entered integer is neither prime nor composite. ")
else:
    test = True
    i=2
    while i <= math.sqrt(abs(num)):
        
        if num%1 ==0:
            test = False
            i=abs(num)
        i = i+1
            
            
        
    