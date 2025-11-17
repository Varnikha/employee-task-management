from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "todo"
    priority: str = "medium"
    assigned_to: Optional[int] = None
    due_date: Optional[datetime] = None

# For creating tasks (POST)
class TaskCreate(TaskBase):
    pass

# For updating tasks (PUT)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[int] = None
    due_date: Optional[datetime] = None

# For responses
class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
       exclude_unset = True