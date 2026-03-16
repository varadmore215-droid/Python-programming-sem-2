# code for receipt
"""
Created on Mon Feb 16 15:04:57 2026

@author: Varad
"""

copies = int(input("Enter number of receipt copies"))
items = int(input("Enter number of  items in each receipt:"))

for copy in range(1, copies + 1):
    print("\nReceipt copy:", copy)
    print("-----------------------------")
    for item in range(1, items + 1):
        print("Item number:", item)
        
        print("-----------------------")
        print("\nAll RECEIPTS PRINTED SUCESSFULLY!")
