import json
import requests
import streamlit as st
from pathlib import Path
from streamlit.logger import get_logger

FASTAPI_BACKEND_ENDPOINT = "http://localhost:8080"
LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Iris Flower Prediction",
        page_icon="chart_with_upwards_trend",
    )
    
    # Sidebar
    with st.sidebar:
        try:
            backend_request = requests.get(FASTAPI_BACKEND_ENDPOINT)
            if backend_request.status_code == 200:
                st.success("Backend online")
            else:
                st.warning("Problem connecting")
        except requests.ConnectionError as ce:
            LOGGER.error(ce)
            st.error("Backend offline")
        
        st.info("Configure parameters")
        
        sepal_length = st.slider("Sepal Length", 4.3, 7.9, 5.0, 0.1, 
                                help="Sepal length in cm", format="%.1f")
        sepal_width = st.slider("Sepal Width", 2.0, 4.4, 3.0, 0.1, 
                               help="Sepal width in cm", format="%.1f")
        petal_length = st.slider("Petal Length", 1.0, 6.9, 3.0, 0.1, 
                                help="Petal length in cm", format="%.1f")
        petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0, 0.1, 
                               help="Petal width in cm", format="%.1f")
        
        predict_button = st.button('Predict')
    
    # Body
    st.write("# Iris Flower Prediction")
    st.write("Adjust the sliders to predict the iris flower species")
    
    if predict_button:
        payload = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
        
        try:
            result_container = st.empty()
            with st.spinner('Predicting...'):
                response = requests.post(
                    f'{FASTAPI_BACKEND_ENDPOINT}/predict',
                    json=payload
                )
            
            if response.status_code == 200:
                prediction = response.json()["response"]
                species = ["Setosa", "Versicolor", "Virginica"]
                result_container.success(f"Predicted species: {species[prediction]}")
            else:
                st.error(f"Error: {response.status_code}")
                
        except Exception as e:
            st.error("Problem with backend. Check if it's running.")
            LOGGER.error(e)

if __name__ == "__main__":
    run()
