# check whether a given year is leap year
"""
Created on Mon Mar 16 15:05:46 2026

@author: Varad
"""

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
 print("Leap Year")
else:
 print("Not a Leap Year")
