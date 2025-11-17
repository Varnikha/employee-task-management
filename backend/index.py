from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user
from routes.task import task
from config.db import meta, engine


app = FastAPI(
    title="Employee & Task Management API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Create all tables
meta.create_all(engine)

# Include routers
app.include_router(user, prefix="/api/employees", tags=["Employees"])
app.include_router(task, prefix="/api/tasks", tags=["Tasks"])

@app.get("/")
def read_root():
    return {
        "message": "Employee & Task Management API",
        "docs": "/docs",
        "employees": "/api/employees",
        "tasks": "/api/tasks"
    }