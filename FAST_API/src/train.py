"""
Model training module for Decision Tree classifier
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from typing import Dict
from .data import prepare_train_test_split, get_target_names

MODEL_PATH = "models/iris_decision_tree_model.joblib"

def train_model(max_depth: int = 4, random_state: int = 42) -> Dict:
    """
    Train a Decision Tree classifier on Iris dataset
    
    Args:
        max_depth: Maximum depth of the decision tree
        random_state: Random seed for reproducibility
        
    Returns:
        Dictionary containing training results and metrics
    """

    X_train, X_test, y_train, y_test = prepare_train_test_split(
        test_size=0.2, 
        random_state=random_state
    )
    

    model = DecisionTreeClassifier(
        max_depth=max_depth,
        random_state=random_state,
        criterion='gini'
    )
    
    model.fit(X_train, y_train)
    

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    

    joblib.dump(model, MODEL_PATH)
    

    target_names = get_target_names()
    report = classification_report(
        y_test, 
        y_test_pred, 
        target_names=target_names,
        output_dict=True
    )
    
    results = {
        "model_saved": MODEL_PATH,
        "train_accuracy": round(train_accuracy, 4),
        "test_accuracy": round(test_accuracy, 4),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "max_depth": max_depth,
        "classification_report": report
    }
    
    return results

def load_model():
    """Load the trained model from disk"""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file '{MODEL_PATH}' not found. Please train the model first."
        )
    return joblib.load(MODEL_PATH)