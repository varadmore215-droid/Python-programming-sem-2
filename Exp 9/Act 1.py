# math module to calculate EMI interest.
"""
Created on Mon Apr 20 09:13:35 2026

@author: Varad
"""
import math

def calculate_emi(p, annual_rate, years):
    
    r = annual_rate / (12 * 100)
    n = years * 12
    numerator = p * r * math.pow(1 + r, n)
    denominator = math.pow(1 + r, n) - 1
    emi = numerator / denominator
    return emi

principal = 50000      
rate = 10.5            
tenure = 2            

emi_result = calculate_emi(principal, rate, tenure)

print(f"Loan Amount: {principal}")
print(f"Annual Interest Rate: {rate}%")
print(f"Tenure: {tenure} years")
print(f"Monthly EMI: {round(emi_result, 2)}")
