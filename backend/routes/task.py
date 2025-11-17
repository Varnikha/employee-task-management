from fastapi import APIRouter, HTTPException, Query
from config.db import conn
from models.index import task as task_table
from schema.task import Task, TaskCreate, TaskUpdate
from typing import List, Optional

task = APIRouter()

@task.post("/", response_model=Task, status_code=201)
async def create_task(task_data: TaskCreate):
    """Create a new task"""
    try:
        query = task_table.insert().values(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            priority=task_data.priority,
            assigned_to=task_data.assigned_to,
            due_date=task_data.due_date
        )
        result = conn.execute(query)
        conn.commit()
        
        new_task = conn.execute(
            task_table.select().where(task_table.c.id == result.lastrowid)
        ).fetchone()
        
        return dict(new_task._mapping)
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@task.get("/", response_model=List[Task])
async def get_all_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = None,
    priority: Optional[str] = None
):
    """Get all tasks with filtering and pagination"""
    query = task_table.select()
    
    if status:
        query = query.where(task_table.c.status == status)
    if priority:
        query = query.where(task_table.c.priority == priority)
    
    query = query.offset(skip).limit(limit)
    result = conn.execute(query).fetchall()
    return [dict(row._mapping) for row in result]


@task.get("/{id}", response_model=Task)
async def get_task_by_id(id: int):
    """Get a single task by ID"""
    query = task_table.select().where(task_table.c.id == id)
    result = conn.execute(query).fetchone()
    
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return dict(result._mapping)


@task.put("/{id}", response_model=Task)
async def update_task(id: int, task_data: TaskUpdate):
    """Update a task"""
    existing = conn.execute(
        task_table.select().where(task_table.c.id == id)
    ).fetchone()
    
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_data.dict(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    try:
        query = task_table.update().where(task_table.c.id == id).values(**update_data)
        conn.execute(query)
        conn.commit()
        
        updated = conn.execute(
            task_table.select().where(task_table.c.id == id)
        ).fetchone()
        
        return dict(updated._mapping)
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@task.delete("/{id}")
async def delete_task(id: int):
    """Delete a task"""
    existing = conn.execute(
        task_table.select().where(task_table.c.id == id)
    ).fetchone()
    
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    
    try:
        query = task_table.delete().where(task_table.c.id == id)
        conn.execute(query)
        conn.commit()
        return {"message": "Task deleted successfully", "id": id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@task.get("/user/{user_id}/tasks", response_model=List[Task])
async def get_user_tasks(user_id: int):
    """Get all tasks assigned to a user"""
    query = task_table.select().where(task_table.c.assigned_to == user_id)
    result = conn.execute(query).fetchall()
    return [dict(row._mapping) for row in result]