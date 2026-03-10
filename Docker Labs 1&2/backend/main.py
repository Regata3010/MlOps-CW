from fastapi import FastAPI
from pydantic import BaseModel
import random
import numpy as np

app = FastAPI(title="MLOps Lab API")

class PredictionRequest(BaseModel):
    feature1: float = 1.0
    feature2: float = 2.0
    feature3: float = 3.0

@app.get("/")
def root():
    return {"message": "MLOps Docker Lab API", "status": "healthy"}

@app.post("/predict")
def predict(request: PredictionRequest):
    # Simple mock ML prediction created for demonstration purposes
    score = random.random()
    return {
        "prediction": "positive" if score > 0.5 else "negative",
        "confidence": score,
        "model": "mock-sentiment-v1"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ml-backend"}