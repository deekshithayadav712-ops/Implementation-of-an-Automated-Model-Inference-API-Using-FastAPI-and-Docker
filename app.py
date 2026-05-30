from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Customer Churn Prediction API", version="1.0")

# Define the expected data format from the client
class CustomerData(BaseModel):
    age: int
    tenure: int
    monthly_charges: float

@app.get("/")
def home():
    return {"message": "Welcome to the Churn Prediction API. Use the /predict endpoint to get scores."}

@app.post("/predict")
def predict_churn(data: CustomerData):
    # Simulated model logic: lower tenure + higher charges = higher risk
    risk_score = (data.monthly_charges / 120.0) * (1.0 - (data.tenure / 72.0))
    risk_score = min(max(risk_score, 0.0), 1.0) # Keep it between 0.0 and 1.0
    
    prediction = 1 if risk_score > 0.5 else 0
    
    return {
        "status": "success",
        "input_received": {
            "age": data.age,
            "tenure": data.tenure,
            "monthly_charges": data.monthly_charges
        },
        "prediction": {
            "churn_probability": round(risk_score, 4),
            "will_churn": prediction
        }
    }
