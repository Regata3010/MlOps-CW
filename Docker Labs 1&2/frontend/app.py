import streamlit as st
import requests
import os

st.set_page_config(page_title="MLOps Docker Lab", page_icon="🐳")
st.title("🐳 MLOps Docker Lab Demo")
st.markdown("### Sentiment Analysis Service")


BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8080")

col1, col2, col3 = st.columns(3)
with col1:
    feature1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
with col2:
    feature2 = st.slider("Feature 2", 0.0, 10.0, 5.0)
with col3:
    feature3 = st.slider("Feature 3", 0.0, 10.0, 5.0)

if st.button("🎯 Get Prediction", type="primary"):
    try:
        response = requests.post(f"{BACKEND_URL}/predict",
            json={"feature1": feature1, "feature2": feature2, "feature3": feature3})
        result = response.json()
        st.success(f"**Prediction:** {result['prediction']}")
        st.info(f"**Confidence:** {result['confidence']:.2%}")
    except:
        st.error("Backend not available - run with docker-compose")
        
        
if st.button("Check Backend Health"):
    try:
        response = requests.get(f"{BACKEND_URL}/health")
        result = response.json()
        st.success(f"Backend Status: {result['status']}")
    except:
        st.error("Backend not available - run with docker-compose")