💳 Credit Card Fraud Detection System

A web-based Credit Card Fraud Detection System that uses Machine Learning to predict whether a transaction is fraudulent or legitimate.

The system is built using Django and integrates a trained ML model from scikit-learn to perform real-time fraud prediction.

The application provides a dashboard where users can input transaction details and receive:

Fraud prediction (Fraud / Not Fraud)

Risk probability score

Visual analytics using charts

📌 Project Overview

Credit card fraud has become a major concern in modern digital payment systems. Financial institutions process millions of transactions daily, making manual fraud detection impossible.

Machine learning techniques can identify patterns in historical transaction data and detect suspicious behavior automatically.

This project demonstrates how machine learning can be integrated with a web application to simulate a real-world fraud detection system.

The system performs the following tasks:

Trains a machine learning model using historical transaction data

Saves the trained model for prediction use

Integrates the model into a Django web application

Allows users to simulate transaction inputs

Displays fraud risk prediction and visual graphs

📊 Dataset

The model is trained using the Credit Card Fraud Detection Dataset (ULB).

Dataset characteristics:

Feature	Description
Time	Seconds elapsed between transactions
V1–V28	PCA-transformed features representing transaction behavior
Amount	Transaction amount
Class	Target label (0 = normal transaction, 1 = fraud)

Dataset statistics:

Total Transactions: 284,807

Fraud Cases: 492

Since fraud cases are very rare, the dataset is highly imbalanced.

🛠 Technology Stack
Backend

Django

Python 3

Machine Learning

scikit-learn

Pandas

NumPy

Joblib

Frontend

HTML

CSS

Chart.js (data visualization)

Development Environment

GitHub Codespaces

Python Virtual Environment

🤖 Machine Learning Model

The system uses Logistic Regression, a widely used classification algorithm for fraud detection.

Training Process

Load dataset (creditcard.csv)

Separate features and target variable

Apply feature scaling using StandardScaler

Split dataset into training and testing sets

Train the Logistic Regression model

Evaluate model performance

Save trained model using Joblib

Saved model files:

fraud_model.pkl
scaler.pkl

These files are later loaded by Django for real-time fraud prediction.

⚙️ System Workflow
Historical Transaction Dataset
            ↓
      Data Preprocessing
            ↓
      Machine Learning Model Training
            ↓
        Save Model (Joblib)
            ↓
        Django Backend
            ↓
     User Inputs Transaction
            ↓
     Fraud Probability Prediction
            ↓
     Dashboard Visualization
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone
cd credit_card_detection
2️⃣ Create Virtual Environment

Create a Python virtual environment to isolate dependencies.

python -m venv venv
3️⃣ Activate Virtual Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate

After activation, your terminal should show:

(venv)
4️⃣ Install Dependencies
pip install django pandas scikit-learn numpy joblib

6️⃣ Run the Django Server
python manage.py migrate
python manage.py runserver

Open in browser:

http://localhost:8000

## Application Features

Machine learning fraud prediction

Interactive dashboard interface

Fraud risk probability score

Graph-based visual analysis

Transaction simulation input

Real-time prediction results

🧪 Test Examples

Use the following inputs to test the system.

Test Case 1 — Normal Transaction
Field	Value
Amount	500
Hour	14
Transaction Type	Offline
Merchant	Grocery
Location	Same City
Recent Transactions	2

Expected Result:

Prediction: NOT FRAUD
Risk Score: Low
Test Case 2 — Normal Online Purchase
Field	Value
Amount	1200
Hour	18
Transaction Type	Online
Merchant	Others
Location	Same City
Recent Transactions	3

Expected Result:

Prediction: NOT FRAUD
Risk Score: Low–Medium
Test Case 3 — Suspicious Transaction
Field	Value
Amount	15000
Hour	1
Transaction Type	Online
Merchant	Electronics
Location	Same City
Recent Transactions	4

Expected Result:

Prediction: Possibly FRAUD
Risk Score: Medium
Test Case 4 — High Risk Transaction
Field	Value
Amount	75000
Hour	2
Transaction Type	Online
Merchant	Electronics
Location	Different City
Recent Transactions	8

Expected Result:

Prediction: FRAUD
Risk Score: High
Test Case 5 — Extreme Transaction Behavior
Field	Value
Amount	1000
Hour	3
Transaction Type	Online
Merchant	Travel
Location	Different City
Recent Transactions	20

Expected Result:

Prediction: FRAUD
Risk Score: Very High