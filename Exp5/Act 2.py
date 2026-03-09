# Store roll numberin sets.find student present in both classes.
"""
Created on Mon Mar  9 15:34:08 2026

@author: Varad
"""

# Roll numbers present in Class A and Class B
class_a = {101, 102, 105, 108, 110}
class_b = {102, 103, 108, 112, 115}

# Find students present in both
present_in_both = class_a.intersection(class_b)

# Alternatively, using the & operator:
# present_in_both = class_a & class_b

print(f"Students present in both: {present_in_both}")
# Output: {102, 108}
