# Find the factorial of a number using loops.
"""
Created on Mon Mar 16 15:08:27 2026

@author: Varad
"""

n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
 fact = fact * i
print("Factorial:", fact)
