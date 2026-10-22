# 🏦 Loan Approval Prediction Web App

An interactive, user-friendly **Streamlit web application** that predicts loan eligibility status based on historical applicant data and financial profiles. The app uses a pre-trained Machine Learning pipeline to evaluate risk parameters instantly.

## 🚀 Features
- **Dynamic Risk Evaluation**: Captures applicant attributes like age, income, employment history, and credit scoring metrics.
- **Automated Preprocessing**: Seamlessly handles real-time inputs, maps dummy-encoded categorical structures, and scales features dynamically using pre-saved pipeline modules.
- **Instant Result Feedback**: Generates rapid approval (`✅ Loan Approved`) or rejection (`🚨 Loan Rejected`) statuses using an intuitive user interface.

## 📁 Project Structure
Ensure your repository files are placed matching the following layout:
```text
├── app.py                # Main Streamlit application file
├── model.pkl             # Pre-trained Machine Learning model 
├── scaler.pkl            # Pre-fitted data scaling/normalization pickle
├── columns.pkl           # Saved list containing original dummy-encoded feature shapes
├── requirements.txt      # Project Python dependencies
└── README.md             # Project documentation (this file)
```

## 🛠️ Installation & Setup

Follow these straightforward steps to run the application locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### Step 2: Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Launch the local web server by executing the following command:
```bash
streamlit run app.py
```
*Your browser should automatically pop open a window displaying the app at `http://localhost:8501`.*

## 📋 Input Metrics Included
- **Applicant Demographics**: Age, Gender, Education Level.
- **Financial Status**: Monthly Income, Home Ownership (Mortgage, Rent, Own, Other).
- **Credit Profile**: Credit Score (300-850 range), Credit History Length, Outstanding Previous Loans.
- **Loan Details**: Loan Amount requested, Interest Rates, and Calculated Loan-to-Income ratios.
