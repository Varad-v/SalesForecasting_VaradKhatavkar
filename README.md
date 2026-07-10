# 📈 End-to-End Sales Forecasting & Demand Intelligence System

An end-to-end Data Science project that predicts future sales demand, detects anomalies, segments products based on demand patterns, and presents business insights through an interactive Streamlit dashboard.

This project was developed as part of the **XYlofy AI Data Science Internship (Week 3 & Week 4 Project)**.

---

## 📌 Project Overview

Retail businesses rely on accurate demand forecasting to optimize inventory, reduce overstocking, prevent stockouts, and improve customer satisfaction.

This project combines **Time Series Forecasting**, **Machine Learning**, **Anomaly Detection**, **Clustering**, and **Business Intelligence** into one complete analytics solution.

---

## 🎯 Objectives

- Forecast future sales using multiple forecasting techniques.
- Compare forecasting model performance.
- Detect unusual sales spikes and drops.
- Segment products based on demand characteristics.
- Provide actionable business insights through an interactive dashboard.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost

---

## 📂 Project Structure

```
SalesForecasting_VaradKhatavkar/

│── app.py
│── train.csv
│── analysis.ipynb
│── requirements.txt
│── README.md
│── summary.pdf

├── pages/
│   ├── 0_Home.py
│   ├── 1_Sales_Overview.py
│   ├── 2_Forecast_Explorer.py
│   ├── 3_Anomaly_Report.py
│   └── 4_Demand_Segments.py

├── charts/
```

---

## 📊 Tasks Completed

### ✅ Data Exploration

- Data loading
- Data cleaning
- Feature engineering
- Time-based analysis

### ✅ Time Series Analysis

- Monthly Sales Trend
- Seasonal Analysis
- Stationarity Testing
- Time Series Decomposition

### ✅ Forecasting Models

- SARIMA
- Facebook Prophet
- XGBoost Regressor

### ✅ Model Comparison

Evaluation Metrics:

- MAE
- RMSE
- MAPE

---

### ✅ Anomaly Detection

- Isolation Forest
- Rolling Z-Score Analysis

---

### ✅ Product Demand Segmentation

- Feature Scaling
- K-Means Clustering
- PCA Visualization

---

### ✅ Interactive Streamlit Dashboard

The dashboard includes:

- 🏠 Home
- 📊 Sales Overview
- 📈 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Demand Segments

---

## 📈 Dashboard Features

### Sales Overview

- KPI Cards
- Monthly Sales Trend
- Sales by Region
- Sales by Category
- Customer Segments
- Interactive Filters

### Forecast Explorer

- Sales Forecast
- Trend Projection
- Forecast Table
- CSV Export

### Anomaly Report

- Isolation Forest Detection
- Monthly Sales Monitoring
- Anomaly Table
- CSV Export

### Demand Segments

- K-Means Clustering
- PCA Visualization
- Product Segmentation
- Cluster Summary

---

## 📷 Dashboard Screenshots

Screenshots are available inside the **charts/** folder.

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/Varad-v/SalesForecasting_VaradKhatavkar.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run app.py
```

---

## 📊 Dataset

Superstore Sales Dataset

Source:
https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

---

## 📈 Business Outcomes

This project helps businesses:

- Improve inventory planning
- Reduce stock shortages
- Identify abnormal sales behavior
- Understand demand patterns
- Support strategic decision-making

---

## 👨‍💻 Author

**Varad Khatavkar**

Artificial Intelligence & Data Science Engineering Student

GitHub:
https://github.com/Varad-v

LinkedIn:
https://www.linkedin.com/in/varad-khatavkar-675575258/

---

## 📜 License

This project is developed for educational and internship purposes.
