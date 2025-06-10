import streamlit as st

st.set_page_config(page_title="Carbon Footprint Estimator", layout="centered")

st.title(" Carbon Footprint Estimator")
st.markdown("### What is Carbon Footprint?")
st.write("""A carbon footprint is the total greenhouse gas (GHG) emissions caused directly or indirectly by an individual, 
organization, event, or product. In other words, it is one measure of the impact their activities are having 
on the environment, and how much they are contributing to climate change. 
It’s measured in kilograms of CO₂ per week (kg/week) in this app.""")

st.markdown("###  Main Emission Sources")
st.write("""- **Direct Emissions:** Emissions that occur from activities directly controlled by the individual or 
organization, such as fuel combustion in vehicles and energy use in buildings. 
- **Indirect Emissions:** Emissions resulting from the production and transportation of goods and 
services used, including:  
- **Supply Chain Emissions:** Emissions produced during the extraction, processing, and 
transportation of raw materials. 
- **Waste Management:** Emissions generated from the disposal or treatment of waste.""")

st.markdown("###  How is it Calculated?")
st.markdown("###  Carbon Emission Factors Table (kg CO₂ per Unit)")

st.markdown("""
| **Source**            | **Formula**                            | **Emission Factor**         | **Unit**                        |
| ----------------------|----------------------------------------|---------------------------- |---------------------------------|
| (1)🔌 Electricity     | electricity_consumed × 0.9             | 0.9                         | per kWh                         |
| (2)🏠 Cooking (LPG)   | number_of_cylinders × 14 × 2.07        | 2.07                        | per cylinder                    |
| (3)✈️ Air             | air_km × 0.121                         | 0.121                       | per km                          |
| (4)🚆 Train           | train_km × 0.0078                      | 0.0078                      | per km                          |
| (5)🚌 Bus             | bus_km × 0.054                         | 0.054                       | per km                          |
| (6)🚗 Car             | car_km × 0.1431                        | 0.1431                      | per km                          |
| (7)🛢️ Petrol          | petrol_liters × 2.34                   | 2.34                        | per liter                       |
| (8)🛢️ Diesel          | diesel_liters × 2.71                   | 2.71                        | per liter                       |

**Total Emissions Calculation Formula:** (1) + (2) + (3) + (4) + (5) + (6) + (7) + (8) kg/week""")

st.markdown("### Prediction Analysis")
st.markdown(""" 
|  **Emission (kg/week)** |  **Prediction**   |
|-------------------------|-------------------|
|    Less than 200        |   LOW             |
|    200 - 800            |   MODERATE        |
|    Greater than 800     |   HIGH            |""")

st.markdown("###  Ways to Reduce Carbon Footprint") 
st.write("""- **Energy Efficiency:** Implementing energy-efficient practices in homes and businesses, such as using 
LED lighting, improving insulation, and optimizing heating and cooling systems. 
- **Sustainable Transportation:** Choosing public transport, biking, walking, or using electric vehicles. 
- **Waste Reduction:** Recycling, composting, and minimizing single-use products contribute to lower 
emissions related to waste management.""") 

st.markdown(" ### Challenges in Reducing Carbon Footprint") 
st.write("""- **Awareness and Education:** Many people are unaware of the extent of their carbon footprints or the 
actions they can take to reduce them. 
- **Behavioral Change:** Shifting long-standing habits and behaviors can be challenging, requiring both 
individual commitment and systemic support. 
- **Economic Factors:** Some sustainable options may be perceived as more expensive upfront, leading 
to resistance to change despite long-term savings.""")

if st.button(" Calculate Now"):
    st.switch_page("Code/Streamlit/pages/1_calculate_CF.py")




