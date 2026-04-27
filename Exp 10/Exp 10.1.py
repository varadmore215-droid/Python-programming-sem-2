# To implement Streamlit applications in Python, specifically:
"""
Created on Mon Apr 27 15:05:19 2026

@author: Varad
"""

import streamlit as st

# Title and header
st.title("Simple Streamlit Application")
st.header("User Input and Display Demo")

# User input widgets
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
color = st.selectbox("Choose your favorite color:", ["Red", "Blue", "Green"])

# Button
if st.button("Submit"):
 st.success("Data submitted successfully!")
 st.write("Name:", name)
st.write("Age:", age)
st.write("Favorite Color:", color)

# Display text and markdown
st.markdown("### This is a Markdown heading")
st.text("This is plain text output")
