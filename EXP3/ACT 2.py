# code for seat booking
"""
Created on Mon Feb 16 15:44:56 2026

@author: Varad
"""
rows = int(input("Enter number of rows:"))
seats_per_rows = int(input("Enter number of seats in each rows:"))
for row in range(1, rows + 1):
    print("Row", row, ":",end=" ")
    for seat in range(1, seats_per_rows + 1):
        print(f"S{seat}", end=" ")
        print()
