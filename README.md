# 🤖 AI Resume Analyzer - Backend

A Django REST Framework backend that provides secure authentication, resume processing, machine learning-based job role prediction, and AI-powered resume feedback using Google's Gemini API.

## 🌐 Live API

https://ai-resume-analyzer-backend-dii1.onrender.com/api/dashboard/
---

## 📌 Features

* RESTful API
* JWT Authentication
* User Registration
* User Login
* Resume Upload
* PDF Text Extraction
* Machine Learning Job Role Prediction
* Google Gemini AI Resume Review
* Resume History
* PostgreSQL Database
* Secure API Endpoints

---

## 🛠️ Tech Stack

### Backend

* Python 3.11
* Django 5
* Django REST Framework
* Simple JWT
* Gunicorn
* WhiteNoise

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* NLTK

### AI

* Google Gemini API

### Database

* PostgreSQL

### Deployment

* Render

---

## 📂 Project Structure

```text
accounts/
jobs/
resume/
ml/
dataset/
config/
manage.py
requirements.txt
```

---

## ⚙️ Installation

Clone repository

```bash
git clone https://github.com/Dhananjayan-maz/ai-resume-analyzer-backend.git
```

Move inside project

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start server

```bash
python manage.py runserver
```

---

## 🔐 Environment Variables

Create a `.env` file

```env
SECRET_KEY=your_secret_key

DEBUG=True

GEMINI_API_KEY=your_gemini_api_key
```

---

## 📡 API Endpoints

### Authentication

POST `/api/register/`

POST `/api/login/`

POST `/api/token/refresh/`

---

### Resume

POST `/api/resume/upload/`

GET `/api/resume/history/`

GET `/api/resume/<id>/`

---

### Dashboard

GET `/api/dashboard/`

---

## 🤖 Machine Learning Workflow

1. Upload Resume PDF
2. Extract Text using PyMuPDF
3. Clean Resume Text
4. Predict Job Role using Scikit-learn Model
5. Send Resume to Gemini AI
6. Receive AI Feedback
7. Store Results in PostgreSQL

---

## 🔗 Frontend Repository

https://github.com/Dhananjayan-maz/ai-resume-analyzer-frontend
---

## 📸 API Testing

The APIs can be tested using:

* Postman
* Django REST Framework Browsable API

---

## 🚀 Future Enhancements

* Resume Matching Score
* ATS Compatibility Checker
* Resume Recommendation Engine
* Email Notifications
* Admin Dashboard
* Docker Deployment
* CI/CD with GitHub Actions

---

## 👨‍💻 Author

**Dhananjayan M**

B.Tech Artificial Intelligence and Data Science

LinkedIn: https://www.linkedin.com/in/dhananjayan-m-5b1a4728b/

GitHub: https://github.com/Dhananjayan-maz

---

⭐ If you found this project useful, consider giving it a star.
