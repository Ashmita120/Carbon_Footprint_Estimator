import streamlit as st
import pandas as pd
import joblib

model = joblib.load("E://Carbon_Footprint_Estimator//random_forest_CF_model.pkl")

st.title("🧮 Carbon Footprint Calculator")

diet = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
heating = st.selectbox("Heating Energy Source", ["Electricity", "Gas", "Wood", "None"])
transport = st.selectbox("Primary Transport Mode", ["Car", "Bus", "Bike", "Walk"])
grocery_bill = st.number_input("Weekly Grocery Bill (₹)", min_value=0)
air_travel = st.number_input("Air Travel Frequency (times/year)", min_value=0)
vehicle_km = st.number_input(" Vehicle Distance (km)", min_value=0)
waste_bags = st.number_input("Waste Bags per Week", min_value=0)
electricity_kwh = st.number_input("Weekly Electricity Usage (kWh)", min_value=0)

if st.button("Predict My CO₂ Emission"):
    input_data = pd.DataFrame([{
        "Diet": diet,
        "Heating Energy Source": heating,
        "Transport": transport,
        "Weekly Grocery Bill": grocery_bill,
        "Frequency of Traveling by Air": air_travel,
        "Vehicle Distance Km": vehicle_km,
        "Waste Bag Weekly Count": waste_bags,
        "Weekly Electricity Usage": electricity_kwh
    }])

    diet_map = {"Vegan": 0, "Vegetarian": 1, "Non-Vegetarian": 2}
    heating_map = {"None": 0, "Electricity": 1, "Gas": 2, "Wood": 3}
    transport_map = {"Walk": 0, "Bike": 1, "Bus": 2, "Car": 3}

    input_data["Diet"] = input_data["Diet"].map(diet_map)
    input_data["Heating Energy Source"] = input_data["Heating Energy Source"].map(heating_map)
    input_data["Transport"] = input_data["Transport"].map(transport_map)

    try:
        prediction = model.predict(input_data)[0]
        st.success(f" Estimated CO₂ Footprint: **{prediction:.2f} kg/week**")

        if prediction > 800:
            st.warning(" High footprint! Consider reducing electricity usage, using public transport and switching to a greener diet.")
        elif prediction >200 and prediction <800:
            st.info(" Moderate footprint! Well done and Keep on trying .")
        else:
            st.balloons()
            st.sucess(" Low footprint! Great job being eco-friendly.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
