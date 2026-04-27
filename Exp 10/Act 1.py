# Create a Streamlit grocery bill calculator.
"""
Created on Mon Apr 27 15:39:26 2026

@author: Varad
"""

import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Grocery Bill Calculator", page_icon="🛒")
    
    st.title("🛒 Grocery Bill Calculator")
    st.write("Add your items below to calculate your total expenses.")

    # Initialize session state for the shopping list
    if 'grocery_list' not in st.session_state:
        st.session_state.grocery_list = []

    # Sidebar for adding items
    with st.sidebar:
        st.header("Add New Item")
        item_name = st.text_input("Item Name", placeholder="e.g., Apples")
        item_price = st.number_input("Price per unit ", min_value=0.0, step=0.01, format="%.2f")
        item_qty = st.number_input("Quantity", min_value=1, step=1)
        
        if st.button("Add to List"):
            if item_name:
                new_item = {
                    "Item": item_name,
                    "Price": item_price,
                    "Quantity": item_qty,
                    "Total": round(item_price * item_qty, 2)
                }
                st.session_state.grocery_list.append(new_item)
                st.success(f"Added {item_name}!")
            else:
                st.error("Please enter an item name.")

    # Main Display Area
    if st.session_state.grocery_list:
        df = pd.DataFrame(st.session_state.grocery_list)
        
        # Display the table
        st.subheader("Your Shopping Cart")
        st.dataframe(df, use_container_width=True)

        # Calculations
        grand_total = df['Total'].sum()
        item_count = df['Quantity'].sum()

        # Display Metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Items", item_count)
        with col2:
            st.metric("Grand Total", f"{grand_total:.2f}")

        # Clear List Button
        if st.button("Clear List"):
            st.session_state.grocery_list = []
            st.rerun()
    else:
        st.info("Your cart is currently empty. Use the sidebar to add items!")

if __name__ == "__main__":
    main()
