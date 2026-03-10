# Docker Labs Assignment - MLOps Course

## What I Built

I created a simple ML prediction app with Docker. It has a backend API that makes predictions and a frontend where users can interact with it.

## My Modifications

Instead of copying the original lab, I made these changes:
- Used FastAPI for the backend 
- Added Streamlit for a better UI
- Created a sentiment analysis predictor
- Used different ports (8080 and 8502)
- Added a health check endpoint

## How to Run

### Option 1: Docker Compose
```bash
git clone https://github.com/yourusername/docker-labs-assignment
cd docker-labs-assignment
docker-compose up
```
Then go to http://localhost:8502

### Option 2: Pull from Docker Hub
```bash
docker pull regata3010/regata-docker:backend
docker pull regata3010/regata-docker:frontend

# Run them
docker network create mynetwork
docker run -d --name backend --network mynetwork -p 8080:8080 regata3010/regata-docker:backend
docker run -d --name frontend --network mynetwork -p 8502:8502 -e BACKEND_URL=http://backend:8080 regata3010/regata-docker:frontend
```

## Project Structure
```
backend/
  - main.py (FastAPI server)
  - requirements.txt
  - Dockerfile
frontend/
  - app.py (Streamlit UI)
  - Dockerfile
docker-compose.yml
README.md
```

## Docker Images

Backend: https://hub.docker.com/r/regata3010/regata-docker (tag: backend)  
Frontend: https://hub.docker.com/r/regata3010/regata-docker (tag: frontend)

## Testing

1. Backend health: http://localhost:8080/health
2. Frontend UI: http://localhost:8502
3. Click "Get Prediction" to test the connection

## Technologies Used
- Python 3.9
- FastAPI for backend API
- Streamlit for frontend UI
- Docker & Docker Compose for containerization

## Notes

This was built for the Docker Labs assignment. I modified it from the original template by changing the ML model type and using different frameworks to make it my own implementation.