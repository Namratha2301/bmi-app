# BMI & Body Fat Percentage Calculator

This Streamlit app calculates your **Body Mass Index (BMI)** and estimates your **Body Fat Percentage** based on user inputs. This tool is for educational purposes only and is not a substitute for professional medical advice.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bmi-app-namratha.streamlit.app)

<img width="1470" alt="Screenshot 2024-11-02 at 4 58 39 PM" src="https://github.com/user-attachments/assets/b6ca9d89-8a2f-4616-bfeb-f6f5a3212595">
<img width="1470" alt="Screenshot 2024-11-02 at 4 58 46 PM" src="https://github.com/user-attachments/assets/11a5308f-ce33-4c6e-a5fd-4b0c3b297100">


## Features

- **BMI Calculation**: Computes BMI based on height and weight inputs and categorizes it according to standard BMI categories:
  - **Underweight**: BMI < 18.5 (Light Blue)
  - **Normal weight**: BMI 18.5–24.9 (Light Green)
  - **Overweight**: BMI 25–29.9 (Gold)
  - **Obesity**: BMI ≥ 30 (Red)
- **Body Fat Percentage Estimation**: Uses the U.S. Navy Method for calculating body fat based on body measurements, with separate formulas for men and women.

## How It Works

1. **BMI Calculation**:
   - Formula: `BMI = Weight (kg) / (Height (m)^2)`
   - Input height in cm and weight in kg, and the app calculates your BMI, displaying a color-coded category for easy interpretation.

2. **Body Fat Percentage Calculation**:
   - Formula: U.S. Navy Method, based on specific body measurements.
   - For **Men**: Requires waist and neck circumference.
   - For **Women**: Requires waist, hip, and neck circumference.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bmi-bodyfat-calculator.git
   cd bmi-bodyfat-calculator
