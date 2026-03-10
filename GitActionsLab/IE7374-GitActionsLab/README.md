# MLOps Lab 1 - GitHub Actions CI/CD Pipeline

## Overview
This lab demonstrates CI/CD implementation using GitHub Actions with automated testing using pytest and unittest frameworks.

## Project Structure
```
IE7374-GitActionsLab/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── data/
├── .gitignore
└── requirements.txt
```

## Setup

### 1. Clone Repository
```bash
git clone <repository_url>
cd IE7374-GitActionsLab
```

### 2. Create Virtual Environment
```bash
python -m venv actionsvenv
source actionsvenv/bin/activate  # Mac/Linux
# or
actionsvenv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running Tests Locally

### Pytest
```bash
pytest test/test_pytest.py
```

### Unittest
```bash
python -m unittest test.test_unittest
```

## Features

### Calculator Functions
- `fun1(x, y)`: Addition
- `fun2(x, y)`: Subtraction
- `fun3(x, y)`: Multiplication
- `fun4(x, y)`: Sum of all operations

### GitHub Actions Workflows
- **pytest_action.yml**: Automated pytest execution on push to main
- **unittest_action.yml**: Automated unittest execution on push to main

Both workflows run on Python 3.8 and upload test results as artifacts.

## CI/CD Pipeline
Every push to the main branch triggers:
1. Checkout code
2. Setup Python environment
3. Install dependencies
4. Run tests
5. Upload test reports
6. Notify success/failure

## Requirements
- Python 3.8+
- pytest

## Screenshots
1) Test with Pytest : ![Pytest Results](screenshots/GA1.png)
2) Test with Unittest : ![Unittest Results](screenshots/GA2.png)

## Author
Arav - Northeastern University
Data Analytics Engineering, MS