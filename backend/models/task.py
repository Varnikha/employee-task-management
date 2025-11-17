from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

task = Table(
    "task", meta,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String(1000)),
    Column("status", String(50), default="todo"),
    Column("priority", String(50), default="medium"),
    Column("assigned_to", Integer, ForeignKey("user.id")),
    Column("due_date", DateTime),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
)