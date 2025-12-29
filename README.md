# 🏠 California House Price Prediction  

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

This project predicts **California housing prices** using **machine learning** based on historical census data.  
A **Random Forest Regressor** is trained to estimate the median house value, and a **Streamlit frontend** allows users to interactively get predictions by entering house details.

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Regressor 🌲  
- **Problem Type:** Regression  
- **Target Variable:** `median_house_value`  
- **Evaluation Metrics:**
  - 📉 RMSE ≈ **49,000**
  - 📊 R² Score ≈ **0.82**

The model explains approximately **82% of the variance** in housing prices.

---

## 📊 Features Used

- Longitude  
- Latitude  
- Housing Median Age  
- Total Rooms  
- Total Bedrooms  
- Population  
- Households  
- Median Income  
- Ocean Proximity  

---

## 🛠️ Tech Stack

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Joblib  
- Streamlit  
- Git & GitHub  

---

## 📁 Project Structure

```text
house-pricing/
│
├── app.py              # Streamlit frontend
├── main.py             # Model training script
├── housing.csv         # Dataset
├── requirements.txt    # Dependencies
├── models/             # Saved models (ignored in Git)
├── env/                # Virtual environment (ignored)
└── README.md


🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/anikeaty08/house-pricing.git
cd house-pricing

2️⃣ Create & activate virtual environment
python -m venv env
env\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train the model
python main.py


This trains the model and saves it locally inside the models/ directory.

🌐 Run the Web App (Streamlit)
streamlit run app.py


Open browser at: http://localhost:8501

Enter house details

Click Predict

Get the estimated house price 💰
