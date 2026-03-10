import pickle
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = Path(__file__).resolve().parent.parent / 'models' / 'iris_model.pkl'

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run train.py first.")
    
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

@app.get("/")
def read_root():
    return {"status": "online", "message": "Iris prediction API"}

@app.post("/predict")
def predict(data: IrisInput):
    try:
        features = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]
        
        prediction = model.predict(features)
        
        return {"response": int(prediction[0])}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}