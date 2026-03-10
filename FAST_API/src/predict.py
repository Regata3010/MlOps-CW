"""
Prediction module for Iris classification
"""
from typing import List, Dict
import numpy as np
from .train import load_model
from .data import get_target_names, get_feature_names

def predict_single(features: List[float]) -> Dict:
    """
    Make prediction for a single iris sample
    
    Args:
        features: List of 4 features [sepal_length, sepal_width, petal_length, petal_width]
        
    Returns:
        Dictionary containing prediction results
    """
    model = load_model()
    feature_names = get_feature_names()
    target_names = get_target_names()
    
   
    if len(features) != 4:
        raise ValueError(f"Expected 4 features, got {len(features)}")
    

    features_array = np.array(features).reshape(1, -1)
    
   
    prediction = model.predict(features_array)[0]
    probabilities = model.predict_proba(features_array)[0]
    
    
    confidence = float(probabilities[prediction])
    
  
    result = {
        "predicted_class": target_names[prediction],
        "predicted_class_id": int(prediction),
        "confidence": round(confidence, 4),
        "probabilities": {
            target_names[i]: round(float(prob), 4) 
            for i, prob in enumerate(probabilities)
        },
        "input_features": {
            feature_names[i]: features[i] 
            for i in range(len(features))
        }
    }
    
    return result

def predict_batch(features_list: List[List[float]]) -> List[Dict]:
    """
    Make predictions for multiple iris samples
    
    Args:
        features_list: List of feature lists
        
    Returns:
        List of prediction dictionaries
    """
    return [predict_single(features) for features in features_list]