import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('laptop_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("💻 Laptop Price Predictor")
st.write("Enter the specifications to estimate laptop price:")

# User inputs
brand = st.selectbox("Brand", ["HP", "Dell", "Apple", "Asus", "Acer"])
ram = st.slider("RAM (GB)", 2, 64, step=2)
weight = st.number_input("Weight (kg)")
touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

# Convert to numeric
touchscreen = 1 if touchscreen == "Yes" else 0

# Dummy encoding for brand (example — replace with your model’s approach)
brand_encoding = {
    "HP": 0,
    "Dell": 1,
    "Apple": 2,
    "Asus": 3,
    "Acer": 4
}

brand_encoded = brand_encoding[brand]

# Final input (must match model's training input structure)
input_data = np.array([[brand_encoded, ram, weight, touchscreen]])

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Laptop Price: ₹{prediction[0]:,.2f}")
