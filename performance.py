import streamlit as st
import joblib
import pandas as pd

# ===== Load models and feature columns for Performance Rating =====
log_reg_perf = joblib.load("performance_rating_model.pkl")
perf_feature_columns = joblib.load('PerformanceRating_feature_columns.joblib')

# ===== Streamlit app =====
st.title('Employee Performance Rating Predictor')

# Sidebar for model selection
model_type = st.sidebar.selectbox('Select Model', ['Logistic Regression'])

# ===== Input form =====
st.header('Employee Information')

# Demographic
col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age', min_value=18, max_value=65, value=30)
    gender = st.selectbox('Gender', ['Male', 'Female'])
with col2:
    marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    overtime = st.selectbox('Overtime', ['No', 'Yes'])

# Job Information
col1, col2 = st.columns(2)
with col1:
    department = st.selectbox('Department', ['Research & Development', 'Sales', 'Human Resources'])
    job_level = st.number_input('Job Level', min_value=1, max_value=5, value=2)
with col2:
    job_role = st.selectbox('Job Role', [
        'Research Scientist', 'Laboratory Technician', 'Sales Executive',
        'Manufacturing Director', 'Healthcare Representative', 'Manager',
        'Sales Representative', 'Research Director'
    ])
    monthly_income = st.number_input('Monthly Income', min_value=1000, max_value=25000, value=5000)

# Work Environment
col1, col2 = st.columns(2)
with col1:
    business_travel = st.selectbox('Business Travel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    work_life_balance = st.number_input('Work Life Balance (1-4)', min_value=1, max_value=4, value=3)
with col2:
    environment_satisfaction = st.number_input('Environment Satisfaction (1-4)', min_value=1, max_value=4, value=3)
    job_satisfaction = st.number_input('Job Satisfaction (1-4)', min_value=1, max_value=4, value=3)

# ===== Create input dictionary =====
input_data = {
    'Age': age,
    'Gender': 1 if gender == 'Female' else 0,
    'MaritalStatus_Divorced': 1 if marital_status == 'Divorced' else 0,
    'MaritalStatus_Married': 1 if marital_status == 'Married' else 0,
    'MaritalStatus_Single': 1 if marital_status == 'Single' else 0,
    'OverTime': 1 if overtime == 'Yes' else 0,
    'Department_Sales': 1 if department == 'Sales' else 0,
    'Department_Human Resources': 1 if department == 'Human Resources' else 0,
    'JobRole_Laboratory Technician': 1 if job_role == 'Laboratory Technician' else 0,
    'JobRole_Manufacturing Director': 1 if job_role == 'Manufacturing Director' else 0,
    'JobRole_Research Director': 1 if job_role == 'Research Director' else 0,
    'JobRole_Research Scientist': 1 if job_role == 'Research Scientist' else 0,
    'JobRole_Sales Executive': 1 if job_role == 'Sales Executive' else 0,
    'JobRole_Sales Representative': 1 if job_role == 'Sales Representative' else 0,
    'JobLevel': job_level,
    'MonthlyIncome': monthly_income,
    'BusinessTravel_Travel_Frequently': 1 if business_travel == 'Travel_Frequently' else 0,
    'BusinessTravel_Travel_Rarely': 1 if business_travel == 'Travel_Rarely' else 0,
    'WorkLifeBalance': work_life_balance,
    'EnvironmentSatisfaction': environment_satisfaction,
    'JobSatisfaction': job_satisfaction,
    # Default values for remaining features (adjust if needed)
    'DailyRate': 800,
    'Education': 2,
    'EducationField_Life Sciences': 1,
    'EducationField_Marketing': 0,
    'EducationField_Medical': 0,
    'EducationField_Other': 0,
    'EducationField_Technical Degree': 0,
    'HourlyRate': 60,
    'JobInvolvement': 3,
    'NumCompaniesWorked': 2,
    'PercentSalaryHike': 15,
    # Note: Do not include PerformanceRating as input here (target variable)
    'RelationshipSatisfaction': 3,
    'StockOptionLevel': 1,
    'TotalWorkingYears': 7,
    'TrainingTimesLastYear': 2,
    'YearsAtCompany': 5,
    'YearsInCurrentRole': 4,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': 3,
    'DistanceFromHome': 10
}

# ===== Prepare DataFrame =====
input_df = pd.DataFrame([input_data])

# Align columns to model's expected features, fill missing with 0
input_df = input_df.reindex(columns=perf_feature_columns, fill_value=0)

# ===== Predict =====
if st.button('Predict Performance Rating'):
    if model_type == 'Logistic Regression':
        prediction = log_reg_perf.predict(input_df)[0]
  

    st.subheader('Prediction Result')
    st.write(f'Predicted Performance Rating: **{prediction}**')