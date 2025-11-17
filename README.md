# 🏢 Employee & Task Management API

A RESTful API backend for managing employees and tasks built with FastAPI and SQLAlchemy.

## 🌟 Features

- **Employee Management API**
  - CRUD operations for employees
  - Track employee information (name, email, phone, department, position, hire date)
  - Email validation
  - Timestamps for creation and updates

- **Task Management API**
  - Create, read, update, delete tasks
  - Set priority levels (Low, Medium, High)
  - Track task status (To Do, In Progress, Completed)
  - Assign tasks to employees
  - Set due dates
  - Full-text search capabilities

- **RESTful Design**
  - Clean API endpoints
  - JSON request/response
  - Proper HTTP status codes
  - Interactive API documentation (Swagger UI)

## 🛠️ Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type hints
- **SQLite** - Database (easily switchable to PostgreSQL/MySQL)
- **Uvicorn** - ASGI server

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-task-management.git
cd employee-task-management
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

The API will be running at: `http://localhost:8000`

### 5. Access API Documentation

Open your browser and visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📚 API Endpoints

### Root
- `GET /` - API information and available endpoints

### Employees

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/employees` | Get all employees |
| GET | `/api/employees/{id}` | Get employee by ID |
| POST | `/api/employees` | Create new employee |
| PUT | `/api/employees/{id}` | Update employee |
| DELETE | `/api/employees/{id}` | Delete employee |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Get all tasks |
| GET | `/api/tasks/{id}` | Get task by ID |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/{id}` | Update task |
| DELETE | `/api/tasks/{id}` | Delete task |

## 📝 Request/Response Examples

### Create Employee

**POST** `/api/employees`

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "department": "Engineering",
  "position": "Software Developer",
  "hire_date": "2024-01-15T00:00:00"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "department": "Engineering",
  "position": "Software Developer",
  "hire_date": "2024-01-15T00:00:00",
  "created_at": "2024-11-18T10:30:00",
  "updated_at": "2024-11-18T10:30:00"
}
```

### Create Task

**POST** `/api/tasks`

```json
{
  "title": "Implement user authentication",
  "description": "Add JWT authentication to the API",
  "status": "todo",
  "priority": "high",
  "assigned_to": 1,
  "due_date": "2024-12-01T17:00:00"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "title": "Implement user authentication",
  "description": "Add JWT authentication to the API",
  "status": "todo",
  "priority": "high",
  "assigned_to": 1,
  "due_date": "2024-12-01T17:00:00",
  "created_at": "2024-11-18T10:35:00",
  "updated_at": "2024-11-18T10:35:00"
}
```

## 📁 Project Structure

```
employee-task-management/
├── backend/
│   ├── config/
│   │   └── db.py              # Database configuration
│   ├── models/
│   │   ├── employee.py        # Employee database model
│   │   └── task.py            # Task database model
│   ├── schemas/
│   │   ├── employee.py        # Employee Pydantic schemas
│   │   └── task.py            # Task Pydantic schemas
│   ├── routes/
│   │   ├── employee.py        # Employee API routes
│   │   └── task.py            # Task API routes
│   ├── main.py                # FastAPI application entry point
│   └── requirements.txt       # Python dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```


---

⭐ Star this repository if you find it helpful!
