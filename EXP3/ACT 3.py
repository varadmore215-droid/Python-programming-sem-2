#Code for Emi calculation 
"""
Created on Mon Feb 16 15:55:31 2026

@author: Varad
"""
principal=float(input("enter principal amount:"))
monthlyintrest=float(input("enter monthly intrest:"))
year=float(input("enter loan tenure (in years):"))
months = year * 12
monthlyintrest = monthlyintrest /100
emi= (principal * monthlyintrest * (1 + monthlyintrest)** months) / ((1 + monthlyintrest))
print("your emi is:", round(emi, 2))
