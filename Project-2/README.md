# StudyHub FastAPI Backend API

A backend API built using FastAPI for managing study tasks, tracking study sessions, and monitoring student productivity progress.

This project was developed as part of DecodeLabs Full Stack Development Internship - Project 2 (Backend API Development).

---

## Features

- Task Management CRUD API
- Study Session Tracking
- Progress Summary API
- Request Validation using Pydantic
- RESTful API Design
- Proper HTTP Status Codes
- Interactive Swagger Documentation
- Modular FastAPI Structure
- Health Check Endpoint

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Project Structure

```bash
studyhub-api/
│── app/
│   ├── main.py
│   ├── schemas.py
│   │
│   └── routes/
│       ├── tasks.py
│       └── sessions.py
│
│── requirements.txt
│── README.md
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/sidd-sharma22/Decodelabs-FullStackDev.git
cd studyhub-api
```

---

### 2. Open Project Folder

```bash
cd Decodelabs-FullStackDev\Project-2\studyhub-api
```

---

### 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run Server

```bash
uvicorn app.main:app --reload
```

Server will run at:

```bash
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates Swagger documentation.

Open:

```bash
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Root Endpoint

### GET /

Returns API status.

Response:

```json
{
  "message": "StudyHub API is running"
}
```

---

# Task APIs

## Get All Tasks

### GET /tasks/

Returns all tasks.

---

## Create Task

### POST /tasks/

Request:

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

Response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

---

## Get Single Task

### GET /tasks/{task_id}

---

## Update Task

### PUT /tasks/{task_id}

---

## Delete Task

### DELETE /tasks/{task_id}

Returns:

- 204 No Content

---

# Session APIs

## Get All Sessions

### GET /sessions/

---

## Create Study Session

### POST /sessions/

Request:

```json
{
  "subject": "Python",
  "duration": 120
}
```

Response:

```json
{
  "id": 1,
  "subject": "Python",
  "duration": 120
}
```

---

# Progress API

## Get Progress Summary

### GET /progress

Response:

```json
{
  "total_tasks": 3,
  "completed_tasks": 2,
  "pending_tasks": 1,
  "total_sessions": 2,
  "total_study_minutes": 210,
  "total_study_hours": 3.5
}
```

---

# Health Check API

## GET /health

Response:

```json
{
  "status": "healthy",
  "message": "StudyHub API is running"
}
```

---

## Validation Features

This project uses Pydantic validation for:

- Required fields
- Minimum/maximum length validation
- Positive integer validation
- Structured API responses

Example:
- Task title must contain at least 3 characters
- Study session duration must be greater than 0

---

## HTTP Status Codes Used

| Status Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Resource Created |
| 204 | No Content |
| 404 | Resource Not Found |
| 422 | Validation Error |

---

## Learning Outcomes

Through this project, the following backend concepts were practiced:

- FastAPI Fundamentals
- REST API Development
- CRUD Operations
- API Validation
- Request & Response Models
- Route Modularization
- HTTP Methods & Status Codes
- Backend Application Structure

---

## Future Improvements

- Database Integration (PostgreSQL)
- User Authentication
- JWT Security
- Persistent Storage
- Deployment
- Docker Support

---

## Internship Context

This project was created for DecodeLabs Full Stack Development Internship - Project 2: Backend API Development. The project focuses on building backend endpoints, handling user input, validating data, and understanding RESTful API concepts.

---

## Author

Siddharth Sharma  
CSE Student | Full Stack Development Intern - DecodeLabs