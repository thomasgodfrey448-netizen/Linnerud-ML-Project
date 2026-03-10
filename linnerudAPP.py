# import libraries for running model
import streamlit as st
import pandas as pd
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression

# Load Dataself
data = load_linnerud(as_frame=True)
X = data.data
y = data.target

# Train model
model = LinearRegression()
model.fit(X, y)

# Project Title
st.title("Linnerud Fitness Prediction System")

# Model Description
st.header("Model Description")

st.write("""
**Dataset Used:**  
The Linnerud dataset from Scikit-learn. It contains physical exercise data and physiological measurements.

**Feature Variables (Exercises):**
- Chins – number of chin-ups
- Situps – number of sit-ups
- Jumps – number of vertical jumps

**Target Variables (Body Measurements):**
- Weight (lbs)
- Waist (inches)
- Pulse (heart rate)

**Machine Learning Algorithm Used:**  
Linear Regression

**Purpose of the Prediction System:**  
The system predicts a person's **Weight, Waist size, and Pulse rate** based on their exercise performance.
""")


# User Input Section
st.header("Enter Exercise Values")

chins = st.number_input("Enter Number of Chins")
situps = st.number_input("Enter Number of Situps")
jumps = st.number_input("Enter Number of Jumps")

# Prediction Section
st.header("Prediction")

# becouse pandas used in prediction use pandas
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Chins": [chins],
        "Situps": [situps],
        "Jumps": [jumps]
    })

    prediction = model.predict(input_data)

    st.subheader("Predicted Results")

    st.write(f"**Predicted Weight:**   {prediction[0][0]:.2f} lbs")
    st.write(f"**Predicted Waist:**    {prediction[0][1]:.2f} inches")
    st.write(f"**Predicted Pulse:**    {prediction[0][2]:.2f} bpm")

    # Refreshing
    if st.button("Refresh"):
        st.rerun()