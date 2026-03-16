# Check whether a given year is a leap year.
"""
Created on Mon Mar 16 14:40:19 2026

@author: Varad
"""

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print("Leap Year")
else:
  print("Not a Leap Year")
