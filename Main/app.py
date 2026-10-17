from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Enterprise Customer Churn Prediction System API")

preprocessor = joblib.load("preprocessor.joblib")
model = joblib.load("best_model.joblib")

class CustomerData(BaseModel):
    Age: float
    Gender: str
    Tenure: float
    Usage_Frequency: float
    Support_Calls: float
    Payment_Delay: float
    Subscription_Type: str
    Contract_Length: str
    Total_Spend: float
    Last_Interaction: float

@app.get("/")
def home():
    return {"message": "Welcome to Customer Churn Prediction API"}

@app.post("/predict")
def predict_churn(customer: CustomerData):
    data_dict = {
        'Age': [customer.Age],
        'Gender': [customer.Gender],
        'Tenure': [customer.Tenure],
        'Usage Frequency': [customer.Usage_Frequency],
        'Support Calls': [customer.Support_Calls],
        'Payment Delay': [customer.Payment_Delay],
        'Subscription Type': [customer.Subscription_Type],
        'Contract Length': [customer.Contract_Length],
        'Total Spend': [customer.Total_Spend],
        'Last Interaction': [customer.Last_Interaction]
    }
    
    input_df = pd.DataFrame(data_dict)
    transformed_data = preprocessor.transform(input_df)
    prediction = model.predict(transformed_data)[0]
    probability = model.predict_proba(transformed_data)[0][1]
    
    return {
        "churn_prediction": int(prediction),
        "churn_risk_score": float(probability),
        "status": "High Risk (Churn)" if prediction == 1 else "Low Risk (Retained)"
    }