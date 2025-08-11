# Employee Analysis Dashboard – Attrition & Performance Rating Prediction

## 📌 Project Overview
This project contains two interactive dashboards built with **Streamlit** for predicting:
1. **Employee Attrition Risk** – Predicts whether an employee is likely to leave.
2. **Employee Performance Rating** – Predicts an employee's performance rating (3 or 4).

The models are trained on HR analytics data with preprocessing and feature engineering steps applied in Jupyter Notebooks, and the resulting models are deployed in Streamlit apps.

---

## 📂 Repository Structure
```
.
├── emp_attrition.ipynb               # Jupyter Notebook for Attrition Model training & preprocessing
├── performance_rating.ipynb               # Jupyter Notebook for Performance Rating Model training & preprocessing
├── attrition.py                     # Streamlit dashboard for Attrition prediction
├── performance.py                     # Streamlit dashboard for Performance Rating prediction
├── logistic_regression_model.pkl # Trained Logistic Regression model for attrition
├── random_forest_model.pkl       # Trained Random Forest model for attrition
├── performance_rating_model.pkl  # Trained Logistic Regression model for performance rating
├── attrition_feature_columns.joblib        # Feature column list for attrition model
├── PerformanceRating_feature_columns.joblib # Feature column list for performance rating model
├── README.md                     # Project documentation (this file)
```

---




```

---

## 🚀 Running the Dashboards

### **Attrition Prediction Dashboard**
```bash
streamlit run attrition.py
```

### **Performance Rating Prediction Dashboard**
```bash
streamlit run performance.py
```

Once started, Streamlit will provide a **local URL** (usually `http://localhost:8501`) where you can interact with the app.

---

## 📊 Model Details

### Attrition Prediction
- Models used: **Logistic Regression** & **Random Forest**
- Feature encoding: Binary + One-Hot Encoding
- Output:  
  - **Low Risk of Attrition** (likely to stay)  
  - **High Risk of Attrition** (likely to leave)  
  - Probability score

### Performance Rating Prediction
- Model used: **Logistic Regression** (trained on ratings 3 and 4)
- Feature encoding: Binary + One-Hot Encoding
- Output: Predicted rating (3 or 4)

---

## 🛠 Improvements & Next Steps
- Improve performance rating predictions by addressing class imbalance using **SMOTE** or more advanced models like **XGBoost**.
- Integrate both dashboards into a single multi-page Streamlit app.
- Deploy to **Streamlit Cloud**, **Heroku**, or **Azure Web App**.
