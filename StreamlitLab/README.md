# Streamlit Lab - Iris Flower Prediction

End-to-end ML application with FastAPI backend and Streamlit frontend for predicting Iris flower species.

## Project Structure
```
StreamlitLab/
├── src/
│   ├── train.py          # Model training script
│   ├── main.py           # FastAPI backend
│   └── Dashboard.py      # Streamlit frontend
├── models/
│   └── iris_model.pkl    # Trained model (generated)
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

### 1. Create Virtual Environment
```bash
python3 -m venv streamlitvenv
source streamlitvenv/bin/activate  # Mac/Linux
# streamlitvenv\Scripts\activate  # Windows
```

### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import sklearn; print(sklearn.__version__)"
# Should show 1.7.2 or higher
```

## Training the Model

Train the Random Forest classifier on the Iris dataset:
```bash
python src/train.py
```

This creates `models/iris_model.pkl` with approximately 95% accuracy.

## Running the Application

### Terminal 1 - Start FastAPI Backend
```bash
cd src
python -m uvicorn main:app --port 8080
```

Backend runs at: http://localhost:8080

### Terminal 2 - Start Streamlit Frontend
```bash
streamlit run src/Dashboard.py
```

Frontend runs at: http://localhost:8501

## Features

- **Model Training**: Custom Random Forest classifier trained on Iris dataset
- **REST API**: FastAPI backend with POST /predict endpoint
- **Interactive UI**: Streamlit dashboard with real-time predictions
- **Health Monitoring**: Backend status indicator in sidebar
- **Parameter Control**: Adjustable sliders for flower measurements

## API Endpoints

- `GET /` - API status check
- `POST /predict` - Predict iris species
  - Request body:
```json
    {
      "sepal_length": 5.0,
      "sepal_width": 3.0,
      "petal_length": 3.0,
      "petal_width": 1.0
    }
```
  - Response:
```json
    {
      "response": 0
    }
```
    (0=Setosa, 1=Versicolor, 2=Virginica)

## Troubleshooting

### scikit-learn Version Mismatch

If you see pickle compatibility errors:
```bash
deactivate
rm -rf streamlitvenv
python3 -m venv streamlitvenv
source streamlitvenv/bin/activate
pip install -r requirements.txt
rm -rf models
mkdir models
python src/train.py
```

### Backend Connection Issues

Ensure FastAPI is running on port 8080 before starting Streamlit.

### Always Use python -m uvicorn

If you encounter environment issues, always start uvicorn with:
```bash
python -m uvicorn main:app --port 8080
```

This ensures the correct Python environment is used.

## Requirements

- Python 3.8+
- scikit-learn 1.7.2+
- FastAPI
- Streamlit
- Uvicorn

## Model Performance

- Algorithm: Random Forest Classifier
- Features: 4 (sepal length, sepal width, petal length, petal width)
- Classes: 3 (Setosa, Versicolor, Virginica)
- Accuracy: ~95% on test set

## Screenshots
1) Setosa : ![Predictions](screenshots/Setosa.png)
2) Versicolor : ![Prediction](screenshots/Versicolor.png)
3) Virginca : [Prediction](screenshots/Virginica.png)


## Author

Arav - Northeastern University  
Data Analytics Engineering, MS