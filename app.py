import streamlit as st
import pandas as pd
import joblib

# =========================
# Load trained model
# =========================
model = joblib.load("models/housing_model.pkl")

st.title("🏠 California House Price Predictor")
st.write("Enter house details below to predict the price.")

# =========================
# User Inputs
# =========================
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=30)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=800)
households = st.number_input("Households", value=300)
median_income = st.number_input("Median Income (×10,000 USD)", value=4.0)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

# =========================
# Predict Button
# =========================
if st.button("Predict House Price"):
    input_data = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated House Price: ${prediction:,.0f}")
