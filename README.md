# StudyHub – Full Stack Development Projects

A complete Full Stack Development project series built during the **DecodeLabs Industrial Training Program**.  
This repository showcases frontend development, backend API engineering, and database integration through a real-world productivity web application called **StudyHub**.

## Live Demo

The Vercel deployed live demo link:

```bash
https://studyhub-decodelabs.vercel.app/
```

---

# Project Overview

StudyHub is a mobile-first productivity web application designed to help students:

- Track study sessions
- Manage goals
- Monitor progress
- Improve focus and productivity

The project was developed in multiple phases as part of the DecodeLabs Full Stack Development training program.

---

# Internship / Training

**DecodeLabs – Industrial Training Program**  
Full Stack Development │ Batch 2026

Projects completed:

- Project 1 – Frontend Development
- Project 2 – Backend API Development
- Project 3 – Database Integration

The training focused on building production-oriented development skills including:

- Responsive frontend engineering
- REST API architecture
- CRUD operations
- Database integration
- Validation and error handling
- Full stack workflow

---

# Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript
- Responsive Web Design

## Backend
- Python
- FastAPI
- REST API

## Database
- PostgreSQL
- SQLAlchemy ORM

## Tools & Deployment
- Git
- GitHub
- Vercel
- VS Code
- Postman

---

# Features

## Frontend Features
- Mobile-first responsive layout
- Modern clean UI
- Semantic HTML structure
- Accessibility-focused design
- Smooth responsive navigation
- Feature cards and CTA sections
- WCAG-friendly structure

## Backend Features
- RESTful API architecture
- CRUD endpoints
- Request validation
- Structured JSON responses
- HTTP status code handling
- FastAPI routing system

## Database Features
- Database schema integration
- Persistent data storage
- CRUD database operations
- SQLAlchemy ORM integration
- Secure data handling

---

# Project Structure

```bash
Decodelabs-FullstackDev/
│
├── Project-1/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── icons/
│   ├── images/
│   │
│   ├── .gitignore
│   └── README.md
│
├── Project-2/
│   ├── studyhub-api/
│   │   ├── app 
│   │   │   ├── main.py
│   │   │   ├── schemas.py
│   │   │   │
│   │   │   └── routes/
│   │   │       ├── tasks.py
│   │   │       └── sessions.py
│   │   │
│   │   └── .gitignore
│   │
│   ├── .gitignore
│   ├── requirements.txt   
│   └── README.md  
│
├── Project-3/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routes.py
│   │
│   ├── venv/
│   ├── Public
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
│
└── README.md
```

---

# Project Phases

## Project 1 – Frontend Development

Built a fully responsive StudyHub landing page focused on:

* Mobile-first design
* Accessibility
* Semantic HTML
* Responsive layouts
* User-friendly UI

### Key Concepts

* Responsive Web Design
* CSS Flexbox & Grid
* Accessibility
* Semantic Structure
* Hamburg Menu

---

## Project 2 – Backend API Development

Developed backend APIs using FastAPI to handle:

* Application logic
* User requests
* API responses
* Validation
* CRUD operations

### Key Concepts

* REST APIs
* HTTP Methods
* FastAPI
* Validation
* JSON responses

---

## Project 3 – Database Integration

Integrated backend services with a database system to enable:

* Data persistence
* CRUD database operations
* Database schema management
* Secure data handling

### Key Concepts

* PostgreSQL Databases
* SQLAlchemy ORM
* Database Relationships
* CRUD Operations
* Data Integrity

---

# API Endpoints

## Example Routes

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| GET    | /              | Home route         |
| GET    | /students      | Fetch all students |
| POST   | /students      | Create student     |
| PUT    | /students/{id} | Update student     |
| DELETE | /students/{id} | Delete student     |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/sidd-sharma22/Decodelabs-FullStackDev.git
```

---

# Backend Setup

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend Server

```bash
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

Simply open:

```bash
index.html
```

Or use VS Code Live Server extension.

---

# Environment Variables

Create a `.env` file:

DATABASE_URL = `postgresql://postgres:my_password@localhost:5432/studyhub_db`

---

# Learning Outcomes

Through these projects, the following concepts were practiced:

* Full Stack Development
* API Development
* CRUD Operations
* Database Integration
* Responsive Design
* FastAPI Architecture
* RESTful Services
* Error Handling
* Git & GitHub Workflow
* Deployment Workflow

---

# Deployment

Frontend deployed using:

* Vercel

Backend can be deployed using:

* Render
* Railway
* PythonAnywhere

---

# Future Improvements

* User Authentication
* JWT Authorization
* Dashboard Analytics
* Dark Mode
* Study Timer
* Task Management
* Docker Support

---

# Repository Topics

```bash
full-stack fastapi python html css javascript rest-api backend frontend database crud responsive-web-design
```

---

# Acknowledgements

Special thanks to:

* DecodeLabs Industrial Training Program
* FastAPI Documentation
* Open Source Community

---

# Author

**Siddharth Sharma**  
CSE Student | Full Stack Development Intern - DecodeLabs

* Email: `siddharthsharma2219@gmail.com`
* GitHub: [https://github.com/sidd-sharma22](https://github.com/sidd-sharma22)
* LinkedIn: [https://www.linkedin.com/in/sidd-sharma22/](https://www.linkedin.com/in/sidd-sharma22/)
* DevFolio: [https://sidd-devfolio.vercel.app/](https://sidd-devfolio.vercel.app/)

---

# License

This project is developed for educational and portfolio purposes under the DecodeLabs Industrial Training Program.