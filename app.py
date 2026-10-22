import streamlit as st
import pandas as pd
import joblib

# Load models and preprocessing components
model = joblib.load("model.pkl")
Expected_col = joblib.load("columns.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Loan Approval Prediction", layout="wide")
st.title("Loan Approval Prediction")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Enter Your Age", min_value=0, max_value=130, step=1, value=18)
    Gender_select = st.selectbox("Gender", ["Male", "Female"])
    Gender = 1 if Gender_select == "Male" else 0
    Person_income = st.number_input("Monthly Income (in $)", min_value=100, max_value=None, value=5000, step=500)
    Employee_Experience = st.number_input("Employee Experience (Years)", min_value=0.0, max_value=60.0, value=5.0, step=0.5)
    Credit_Score = st.number_input("Credit Score", min_value=300, max_value=850, value=680, step=1)
    Credit_History = st.number_input("Credit History Length (Years)", min_value=0, max_value=40, value=5, step=1)
    Education = st.selectbox("Highest Education Level", ["Associate", "Bachelor", "Doctorate", "High School", "Master"])
    Home_Ownership = st.selectbox("Home Ownership Status", ["MORTGAGE", "OTHER", "OWN", "RENT"])

with col2:
    Loan_Intent = st.selectbox("Loan Purpose / Intent", ["DEBT CONSOLIDATION", "EDUCATION", "HOME IMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
    Loan_Amount = st.number_input("Requested Loan Amount ($)", min_value=0.0, value=10000.0, step=500.0)
    Loan_Interest_Rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, max_value=100.0, value=10.5, step=0.1)
    
    default_pct = (Loan_Amount / Person_income) if Person_income > 0 else 0.0
    Loan_Percentage = st.number_input("Loan-to-Income Percentage (Ratio)", min_value=0.0, max_value=1.0, value=min(default_pct, 1.0), step=0.01)
    Previous_Loan_select = st.radio("Has a Previous Loan?", ["No", "Yes"], horizontal=True)

raw_data = pd.DataFrame([{
    "Age": Age,
    "Gender": Gender,
    "Education_"+Education: 1,
    "Person Income": Person_income,
    "Employee Experience": Employee_Experience,
    "Home Onwership_"+ Home_Ownership: 1,
    "Loan Amount": Loan_Amount,
    "Loan Intent": Loan_Intent,
    "Loan interest Rate": Loan_Interest_Rate,
    "Loan percentage": Loan_Percentage,
    "Credit History": Credit_History,
    "Credit Score": Credit_Score,
    "Previous Loan_"+ Previous_Loan_select: 1
}])
df= pd.DataFrame(raw_data)
for col in Expected_col:
    if col not in df.columns:
        df[col] = 0
df = df[Expected_col]

scaled_features = scaler.transform(df)

st.markdown("---")
if st.button("Predict Loan Status", type="primary"):
    prediction = model.predict(scaled_features)

    
    if prediction[0] == 1:
        st.success(f"✅ Loan Approved")
    elif prediction[0]==0:
        st.error(f"🚨 Loan Rejected")