# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model/discount_model.pkl")

class CustomerData(BaseModel):
    age: int
    signup_channel: str
    device_type: str
    location: str
    browsing_time_minutes: int
    referral_code_used: int
    cart_value: int

@app.post("/predict/")
def predict(data: CustomerData):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)
    return {"recommended_discount": int(pred[0])}
