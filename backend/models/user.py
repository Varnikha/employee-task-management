# models/user.py
from sqlalchemy import Table, Column, Integer, String, DateTime
from config.db import meta, engine
from datetime import datetime

user = Table(
    "user", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255), unique=True),
    Column("phone", String(255)),
    Column("department", String(255)),
    Column("position", String(255)),
    Column("hire_date", DateTime),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
)