from fastapi import APIRouter, HTTPException, Query
from config.db import conn
from models.index import user as user_table
from schema.user import Employee, EmployeeCreate, EmployeeUpdate
from typing import List

user = APIRouter()

@user.post("/", response_model=Employee, status_code=201)
async def create_user(user_data: EmployeeCreate):
    """Create a new user/employee"""
    try:
        query = user_table.insert().values(
            name=user_data.name,
            email=user_data.email,
            phone=user_data.phone,
            department=user_data.department,
            position=user_data.position,
            hire_date=user_data.hire_date
        )
        result = conn.execute(query)
        conn.commit()
        
        new_user = conn.execute(
            user_table.select().where(user_table.c.id == result.lastrowid)
        ).fetchone()
        
        return dict(new_user._mapping)
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@user.get("/", response_model=List[Employee])
async def get_all_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """Get all users with pagination"""
    query = user_table.select().offset(skip).limit(limit)
    result = conn.execute(query).fetchall()
    return [dict(row._mapping) for row in result]


@user.get("/{id}", response_model=Employee)
async def get_user_by_id(id: int):
    """Get a single user by ID"""
    query = user_table.select().where(user_table.c.id == id)
    result = conn.execute(query).fetchone()
    
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    
    return dict(result._mapping)


@user.put("/{id}", response_model=Employee)
async def update_user(id: int, user_data: EmployeeUpdate):
    """Update a user"""
    existing = conn.execute(
        user_table.select().where(user_table.c.id == id)
    ).fetchone()
    
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = user_data.dict(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    try:
        query = user_table.update().where(user_table.c.id == id).values(**update_data)
        conn.execute(query)
        conn.commit()
        
        updated = conn.execute(
            user_table.select().where(user_table.c.id == id)
        ).fetchone()
        
        return dict(updated._mapping)
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@user.delete("/{id}")
async def delete_user(id: int):
    """Delete a user"""
    existing = conn.execute(
        user_table.select().where(user_table.c.id == id)
    ).fetchone()
    
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        query = user_table.delete().where(user_table.c.id == id)
        conn.execute(query)
        conn.commit()
        return {"message": "User deleted successfully", "id": id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))