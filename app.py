# This app is for educational purposes only. Insights gained are not medical advice. Use at your own risk!
import streamlit as st
from PIL import Image
import pandas as pd
import math

#---------------------------------#
# Title and Logo
logo = Image.open('logo.png')  # Make sure logo.png is in the same directory
st.image(logo, width=200)

st.title('BMI & Body Fat Percentage Calculator')
st.markdown("""
This app calculates your Body Mass Index (BMI) and estimates your body fat percentage based on your inputs.
""")

#---------------------------------#
# Sidebar + Main panel
st.sidebar.header('Input Options')

# Sidebar - Input fields for BMI calculation
height = st.sidebar.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, step=0.1)
weight = st.sidebar.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=0.1)
age = st.sidebar.number_input("Enter your age:", min_value=1, max_value=120, step=1)
gender = st.sidebar.selectbox("Select your gender:", ["Male", "Female"])

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Function to determine BMI category and color
def bmi_category_and_color(bmi):
    if bmi < 18.5:
        return "Underweight", "#ADD8E6"  # Light blue
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "#90EE90"  # Light green
    elif 25 <= bmi < 29.9:
        return "Overweight", "#FFD700"  # Gold
    else:
        return "Obesity", "#FF6347"  # Tomato red

category, color = bmi_category_and_color(bmi)

# Display BMI result with color-coded category
st.header("BMI Calculation")
st.write(f"Your BMI is: {bmi:.2f}")
st.markdown(f"<h3 style='color:{color};'>Category: {category}</h3>", unsafe_allow_html=True)

# Sidebar - Input fields for Body Fat Percentage calculation
if gender == "Male":
    waist = st.sidebar.number_input("Enter your waist circumference (in cm):", min_value=20.0, max_value=200.0, step=0.1)
    neck = st.sidebar.number_input("Enter your neck circumference (in cm):", min_value=10.0, max_value=60.0, step=0.1)
    body_fat_percentage = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
else:
    waist = st.sidebar.number_input("Enter your waist circumference (in cm):", min_value=20.0, max_value=200.0, step=0.1)
    neck = st.sidebar.number_input("Enter your neck circumference (in cm):", min_value=10.0, max_value=60.0, step=0.1)
    hip = st.sidebar.number_input("Enter your hip circumference (in cm):", min_value=20.0, max_value=200.0, step=0.1)
    body_fat_percentage = 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height)) - 450

st.header("Body Fat Percentage")
st.write(f"Estimated Body Fat Percentage: {body_fat_percentage:.2f}%")

#---------------------------------#
# About
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python libraries:** streamlit, PIL, math
* **BMI Formula:** Weight (kg) / (Height (m)^2)
* **Body Fat Percentage Formula:** U.S. Navy Method based on body measurements
""")
