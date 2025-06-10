
# 🌱 Carbon Footprint Estimator using Machine Learning

This project aims to estimate weekly carbon emissions (CO₂ kg/week) based on lifestyle inputs like diet, transport, and electricity usage using machine learning regression models.

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://carbonfootprintestimator-ashmita54.streamlit.app/)

## 🎥 Video Walkthrough

Link: [(https://drive.google.com/file/d/13N5guG7-sKtBtmhSEIDxSA2E_zaSI4TQ/view?usp=sharing)]

## 🧠 What is a Carbon Footprint?

A carbon footprint is the total amount of greenhouse gases (GHGs), especially carbon dioxide (CO₂), released into the atmosphere as a result of human activities. It is typically measured in kilograms or tons of CO₂ equivalent (kg CO₂e).


## 🛑 Major Sources of Carbon Emissions

1. **Transportation** – Cars, flights, public transport.
2. **Diet** – Consumption of meat, dairy, or plant-based food.
3. **Electricity & Energy Use** – From non-renewable sources.
4. **Goods and Services** – Manufacturing, shopping, packaging, etc.


## 🔍 Methodology: CO₂ Calculation

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

**Total Emissions Calculation Formula:** (1) + (2) + (3) + (4) + (5) + (6) + (7) + (8) kg/week

The machine learning models learn from past patterns and predict future CO₂ output.


## 📁 Dataset Used
- Carbon_Emission_Data.csv - KAGGLE

## 📊 Approach Used

**1. Data Understanding & Cleaning:** 
- Analyzed the carbon emission dataset and selected relevant features related to electricity use, transportation, diet, waste generation, and fuel usage.

- Handled missing values and encoded categorical features using LabelEncoder for consistent model input.

**2. Feature Selection:**

- Chose core lifestyle indicators for model training that strongly impact personal emissions:

- Diet, Heating Source, Transport, Grocery Bill, Air Travel Frequency, Vehicle Distance, Waste Bag Count, Electricity Usage

**3. Model Building:**

- Trained three regression models: Linear Regression, Decision Tree, and Random Forest.

- Evaluated each using MSE, MAE, and R² score, and selected the best-performing model by considering the lowest MSE.

- Saved the final model using joblib for reuse in Streamlit.

**4. Model Explainability:**

- Visualized feature correlations using heatmaps.
-  Actual vs Predicted Plot

**5. User Interface (Streamlit):**

- Developed a multi-page web app.

- Home Page introduces carbon footprint concepts and sources.

- Calculator Page allows users to enter lifestyle inputs and receive:

- Estimated CO₂ footprint

- Predictions: low, moderate, or high

- Suggestions to reduce emissions.


## 📉 Results

| Model            |   MSE ↓     |   R² ↑ |   MAE ↓  |
|------------------|-------------|--------|----------|
| Linear Regression| 22271.9085 | 0.4645 | 116.9935 |
| Decision Tree    | 30161.5925 | 0.2748 | 123.0593 |
| Random Forest    | 15511.6998  | 0.6270 | 89.0394 |

**Best Model:** Random Forest -> MSE: 15511.6998 (Lowest MSE)


## ✅ How to Reduce Your Carbon Footprint

| Action                          | Estimated Reduction (kg/week) |
|---------------------------------|-------------------------------|
| Switch to plant-based diet      | ~10–20 kg                     |
| Use public transport or bike    | ~30 kg                        |
| Reduce electricity consumption  | ~10–50 kg                     |
| Avoid flights                   | ~100–200 kg per trip          |


## ⚠️ Challenges in reducing carbon footprint

- **1. Lack of Awareness:** Many individuals and even organizations are unaware of the extent of their carbon footprint or what activities contribute most to it.
- **2. Economic Constraints:** Switching to eco-friendly alternatives (e.g., electric vehicles, solar panels, energy-efficient appliances) often requires high upfront costs, which can be a barrier for many households and businesses.
- **3. Limited Access to Alternatives:** In some regions, sustainable options like public transport, organic food, or renewable energy may not be available or practical.
- **4. Behavioral Inertia:** People tend to stick to habitual lifestyles. Changing dietary habits, daily commuting, or purchasing decisions takes time, motivation, and education.
- **5. Policy and Regulation Gaps:** In many countries, government incentives, regulations, or penalties related to carbon emissions are either weak or poorly enforced..


## 🧠 Conclusion

This project demonstrates how machine learning models can estimate an individual's carbon footprint based on key lifestyle indicators. The model can be integrated into sustainability dashboards, mobile apps, or used for awareness campaigns.

## ➡️ References

- **WIKIPEDIA:**   https://en.wikipedia.org/wiki/Carbon_footprint
- **TATA SUSTAINABILITY GROUP:** https://www.tatasustainability.com/Environment/CarbonCalculator
- **EARTH.ORG:**   https://earth.org/what-does-carbon-footprint-mean/
- **ECOLOGI.COM:** https://ecologi.com/articles/blog/what-is-a-carbon-footprint-and-how-is-it-measured
- **BRITANNICA:**  https://www.britannica.com/science/carbon-footprint

## 🧰 Dependencies

To run this project, make sure you have the following Python libraries installed:

| Library        | Purpose                                  |
|----------------|------------------------------------------|
| `streamlit`    | Web app UI framework                     |
| `pandas`       | Data handling and input preprocessing    |
| `numpy`        | Numerical operations                     |
| `scikit-learn` | Machine learning models & preprocessing  |
| `joblib`       | Saving and loading the trained model     |
| `matplotlib`   | Visualization support                    |
| `seaborn`      | Correlation heatmaps, visuals            |


### 🔧 Installation

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

## 📁 Files

- `Carbon_Emission_Data.csv` – Dataset
- `Carbon_Footprint_Estimator.ipynb` – Notebook
- `random_forest_CF_model.pkl` – Trained model
- `README.md` – This file
- `requirements.txt` – Dependencies
