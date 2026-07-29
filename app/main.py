from fastapi import FastAPI
from app.ml.predict import predict_log

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Security Analyzer Running"}

@app.post("/predict")
def predict(log: str):
    return predict_log(log)