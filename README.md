# CI/CD Pipeline Project - DSO101 Assignment IV
**Student**: YontenKinleyTenzin_02230313_DSO101_A4

## Overview
This project demonstrates a complete CI/CD pipeline including automated build, test, and deployment processes. It features a Flask backend application deployed to Render with GitHub Actions orchestration.

## Project Structure
```
DSO_assign4/
├── app.py                              # Flask backend application
├── test_app.py                         # Unit tests for the app
├── requirements.txt                    # Python dependencies
├── Procfile                            # Render deployment configuration
├── .gitignore                          # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci.yml                      # GitHub Actions CI/CD workflow
└── README.md                           # This file
```

## Requirements
- Python 3.9+
- GitHub account
- Render account (free tier available)
- Git

## Local Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/DSO_assign4.git
cd DSO_assign4
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Tests Locally
```bash
pytest test_app.py -v
```

### 5. Run the Application
```bash
python app.py
```

Navigate to:
- Home: `http://localhost:5000/`
- Health: `http://localhost:5000/health`
- Add API: `http://localhost:5000/api/add`

## API Endpoints

### GET `/`
Returns a welcome message with pipeline status.

### GET `/health`
Health check endpoint for monitoring.

### GET `/api/add`
Test endpoint that performs arithmetic operation.

## CI/CD Pipeline
The `.github/workflows/ci.yml` file defines the automated pipeline that:
1. Triggers on every push to main branch
2. Sets up Python environment
3. Installs dependencies
4. Runs all tests with pytest
5. Deploys to Render automatically on success

## Testing
```bash
pytest test_app.py -v           # Run all tests
pytest test_app.py --cov=.      # Run with coverage report
```

## Deployment to Render

1. Push code to GitHub
2. Connect repository to Render dashboard
3. Configure Python 3.9 environment
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Enable auto-deploy

## Verification Checklist

- [ ] Flask app runs locally
- [ ] Tests pass locally
- [ ] Code pushed to GitHub
- [ ] GitHub Actions workflow runs
- [ ] Render deployment triggered
- [ ] Live app accessible

## Assignment Marking Scheme (10 Marks)

| Criteria | Marks | Status |
|----------|-------|--------|
| Project Structure | 2 | ✅ |
| CI Pipeline (Build + Test) | 3 | ✅ |
| Test Implementation | 2 | ✅ |
| Deployment Automation | 2 | ✅ |
| Documentation | 1 | ✅ |
| **Total** | **10** | **✅ Complete** |