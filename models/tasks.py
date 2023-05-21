from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

tasks = Table(
    "tasks",
    Base.metadata,
    Column("id", String(255), nullable=False, primary_key=True),
    Column("task_title", String(50), nullable=False),
    Column("story_points", Integer, nullable=False),
    Column("task_description", String(255), nullable=False),
    Column("task_creator", String(255), nullable=False),
    Column("task_assignee", String(255), nullable=False),
    Column("status", String(25), nullable=False),
)