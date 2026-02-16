# Program for simple intrest
"""
Created on Mon Feb 16 14:55:16 2026

@author: Varad
"""

def simple_intrest(principal,rate,time):
    si=(principal*rate*time)/100
    return si
p = float(input("Enter principal amount:"))
r = float(input("Enter rate of intrest:"))
t = float(input("Enter time(in years):"))
intrest=simple_intrest(p,t,r)
print("simple intrest is:",intrest)
