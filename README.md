# User Management REST API

A lightweight **User Management REST API** built using **Python and FastAPI**, implementing full **CRUD operations**, input validation, unit testing, and Docker-based deployment.  
This project demonstrates backend software development skills including **API design, clean architecture, testing, debugging, and containerization**.

---

## 🚀 Features
- Create, Read, Update, Delete (CRUD) users
- RESTful API design
- Input validation using Pydantic
- Error handling with proper HTTP status codes
- Unit tests using Pytest
- Dockerized for consistent deployment
- Interactive API documentation via Swagger UI

---

## 🛠️ Tech Stack
- **Language:** Python 3.10  
- **Framework:** FastAPI  
- **Validation:** Pydantic  
- **Testing:** Pytest  
- **Containerization:** Docker  
- **Server:** Uvicorn  

---

## 📁 Project Structure

```
user-management-api/
│
├── app/
│ ├── main.py # FastAPI application
│ ├── models.py # Data models
│ ├── crud.py # Business logic
│
├── tests/
│ ├── test_users.py # Unit tests
│ ├── conftest.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```
---

## ▶️ Running the Application (Local)

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
uvicorn app.main:app --reload
```
http://127.0.0.1:8000/docs
```
Use the interactive UI to test all API endpoints.

---

## 🔍 API Endpoints

Method	    Endpoint	    Description

POST	      /users	      Create a new user
GET	        /users	      Retrieve all users
PUT	        /users/{id}	  Update user details
DELETE	    /users/{id}	  Delete a user

