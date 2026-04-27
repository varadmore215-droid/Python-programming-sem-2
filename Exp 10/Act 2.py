# Create a BMI health checker app.
"""
Created on Mon Apr 27 15:57:57 2026

@author: Varad
"""

import streamlit as st

def calculate_bmi(weight, height_m):
    return weight / (height_m ** 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "green"
    elif 25 <= bmi < 30:
        return "Overweight", "orange"
    else:
        return "Obese", "red"

def main():
    st.set_page_config(page_title="BMI Health Checker", page_icon="⚖️")
    
    st.title("⚖️ BMI Health Checker")
    st.write("Body Mass Index (BMI) is a measure of body fat based on height and weight.")

    # Unit Selection
    unit_system = st.radio("Choose Unit System:", ("Metric (kg/cm)", "Imperial (lbs/in)"))

    col1, col2 = st.columns(2)

    if unit_system == "Metric (kg/cm)":
        with col1:
            weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
        with col2:
            height_cm = st.number_input("Height (cm)", min_value=50.0, value=170.0)
        height_m = height_cm / 100
    else:
        with col1:
            weight_lbs = st.number_input("Weight (lbs)", min_value=1.0, value=150.0)
        with col2:
            height_in = st.number_input("Height (inches)", min_value=20.0, value=67.0)
        # Conversion: weight in kg, height in meters
        weight = weight_lbs * 0.453592
        height_m = height_in * 0.0254

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height_m)
        category, color = get_category(bmi)

        st.divider()
        
        # Display Result
        st.subheader("Your Results")
        st.metric(label="Your BMI", value=f"{bmi:.1f}")
        
        # Color-coded status message
        if color == "green":
            st.success(f"Category: **{category}**")
        elif color == "blue" or color == "orange":
            st.warning(f"Category: **{category}**")
        else:
            st.error(f"Category: **{category}**")

        # Health Advice
        st.info("💡 **Note:** BMI is a useful starting point, but it doesn't account for muscle mass, bone density, or overall body composition.")

if __name__ == "__main__":
    main()
