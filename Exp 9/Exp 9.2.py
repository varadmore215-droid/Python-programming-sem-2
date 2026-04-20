#date time module to print the currentdate, time, and weekday
"""
Created on Mon Apr 20 09:11:31 2026

@author: Varad
"""
import datetime
# Get current date and time
now = datetime.datetime.now()
# Print current date
print("Current Date:", now.strftime("%Y-%m-%d"))
# Print current time
print("Current Time:", now.strftime("%H:%M:%S"))

# Print current weekday
print("Weekday:", now.strftime("%A"))
