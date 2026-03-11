# import libraries for running model
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
data = load_linnerud(as_frame=True)
X = data.data
y = data.target

# Train model
model = LinearRegression()
model.fit(X, y)

# Project Title
st.title("Linnerud Fitness Prediction Model")

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
chins = st.number_input("Enter Number of Chins", min_value=0)
situps = st.number_input("Enter Number of Situps", min_value=0)
jumps = st.number_input("Enter Number of Jumps", min_value=0)

# Prediction Section
st.header("Prediction")

if st.button("Predict"):

    # Prepare input data
    input_data = pd.DataFrame({
        "Chins": [chins],
        "Situps": [situps],
        "Jumps": [jumps]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Transparent Prediction Table
    st.subheader("Predicted Results")

    predicted_values = {
        "Measurement": ["Weight (lbs)", "Waist (inches)", "Pulse (bpm)"],
        "Prediction": [round(prediction[0][0],2), round(prediction[0][1],2), round(prediction[0][2],2)]
    }
    df_pred = pd.DataFrame(predicted_values)

    # Display transparent table
    st.markdown(
        df_pred.to_html(index=False, classes='transparent-table', border=0),
        unsafe_allow_html=True
    )

    # Custom CSS for transparent table
    st.markdown("""
        <style>
        .transparent-table {
            width: 100%;
            border-collapse: collapse;
            margin: auto;
            font-size: 16px;
        }
        .transparent-table th {
            color: white;
            text-align: center;
            padding: 8px;
        }
        .transparent-table td {
            background-color: transparent;
            text-align: center;
            padding: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Plotting predicted vs actual dataset values for reference
    st.subheader("Comparison with Dataset")
    targets = ['Weight', 'Waist', 'Pulse']

    for i, target in enumerate(targets):
        st.subheader(f"{target}: Prediction vs Dataset")
        plt.figure(figsize=(5,4))
        # Plot actual dataset values
        sns.scatterplot(x=y[target], y=y[target], color='gray', label='Dataset')
        # Plot predicted point
        plt.scatter(prediction[0][i], prediction[0][i], color='red', s=100, label='Prediction Value')
        # Optional diagonal line y=x
        plt.plot([y[target].min(), y[target].max()],
                 [y[target].min(), y[target].max()],
                 'r--', linewidth=1)
        plt.xlabel("Actual " + target)
        plt.ylabel("Predicted " + target)
        plt.title(f"{target}: Prediction vs Dataset")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
# daily use of model 
st.header("Real-world applications of the model")
st.write(""" 
The Model predict physiological measurements based on exercise performance. This can be applied in

- Fitness Assessment Tools
- Exercise Recommendation Systems
        """
)