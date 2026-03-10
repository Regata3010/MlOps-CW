"""
FastAPI application for Iris classification
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Dict
import os

from .train import train_model, MODEL_PATH
from .predict import predict_single, predict_batch
from .data import get_target_names, get_feature_names


app = FastAPI(
    title="Iris Classification API",
    description="Decision Tree classifier for Iris dataset",
    version="1.0.0"
)

class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., ge=0, le=10, description="Sepal length in cm")
    sepal_width: float = Field(..., ge=0, le=10, description="Sepal width in cm")
    petal_length: float = Field(..., ge=0, le=10, description="Petal length in cm")
    petal_width: float = Field(..., ge=0, le=10, description="Petal width in cm")
    
    def to_list(self) -> List[float]:
        return [
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width
        ]

class BatchPredictionRequest(BaseModel):
    samples: List[IrisFeatures]
    
    @validator('samples')
    def check_samples_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError("samples list cannot be empty")
        return v

class TrainRequest(BaseModel):
    max_depth: int = Field(default=4, ge=1, le=20, description="Maximum depth of decision tree")
    random_state: int = Field(default=42, description="Random seed for reproducibility")

# API Endpoints

@app.get("/", tags=["General"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Iris Classification API",
        "version": "1.0.0",
        "model_status": "trained" if os.path.exists(MODEL_PATH) else "not trained",
        "endpoints": {
            "train": "/train",
            "predict": "/predict",
            "predict_batch": "/predict/batch",
            "info": "/info"
        }
    }

@app.get("/info", tags=["General"])
async def get_info():
    """Get information about the dataset and model"""
    return {
        "dataset": "Iris",
        "features": get_feature_names(),
        "target_classes": get_target_names(),
        "model_type": "Decision Tree Classifier",
        "model_trained": os.path.exists(MODEL_PATH)
    }

@app.post("/train", tags=["Training"])
async def train(request: TrainRequest = TrainRequest()):
    """
    Train the Decision Tree model on Iris dataset
    
    Parameters:
    - max_depth: Maximum depth of the tree (default: 4)
    - random_state: Random seed for reproducibility (default: 42)
    """
    try:
        results = train_model(
            max_depth=request.max_depth,
            random_state=request.random_state
        )
        return {
            "status": "success",
            "message": "Model trained successfully",
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")

@app.post("/predict", tags=["Prediction"])
async def predict(features: IrisFeatures):
    """
    Predict the iris species for a single sample
    
    Parameters:
    - sepal_length: Sepal length in cm
    - sepal_width: Sepal width in cm
    - petal_length: Petal length in cm
    - petal_width: Petal width in cm
    """
    try:
        result = predict_single(features.to_list())
        return {
            "status": "success",
            "prediction": result
        }
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=400, 
            detail="Model not trained. Please train the model first using /train endpoint"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post("/predict/batch", tags=["Prediction"])
async def predict_batch_endpoint(request: BatchPredictionRequest):
    """
    Predict iris species for multiple samples
    
    Parameters:
    - samples: List of iris feature sets
    """
    try:
        features_list = [sample.to_list() for sample in request.samples]
        results = predict_batch(features_list)
        return {
            "status": "success",
            "predictions": results,
            "count": len(results)
        }
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=400, 
            detail="Model not trained. Please train the model first using /train endpoint"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction failed: {str(e)}")

@app.get("/health", tags=["General"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": os.path.exists(MODEL_PATH)
    }