"""
Data loading and preprocessing module for Iris dataset
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from typing import Tuple

def load_iris_data() -> Tuple[pd.DataFrame, pd.Series]:
    """
    Load the Iris dataset from sklearn
    
    Returns:
        Tuple of (features DataFrame, target Series)
    """
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='species')
    
    return X, y

def get_feature_names() -> list:
    """Get the feature names for the Iris dataset"""
    iris = load_iris()
    return iris.feature_names

def get_target_names() -> list:
    """Get the target class names for the Iris dataset"""
    iris = load_iris()
    return iris.target_names.tolist()

def prepare_train_test_split(test_size: float = 0.2, random_state: int = 42):
    """
    Load data and split into train/test sets
    
    Args:
        test_size: Proportion of dataset to include in test split
        random_state: Random seed for reproducibility
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    X, y = load_iris_data()
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=test_size, 
        random_state=random_state,
        stratify=y
    )
    
    return X_train, X_test, y_train, y_test