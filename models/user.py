from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user = Table(
    "user",
    Base.metadata,
    Column("id", String(255), nullable=False, primary_key=True),
    Column("type", String(10), nullable=False),
    Column("username", String(50), nullable=False),
    Column("email", String(50), nullable=False),
    Column("age", Integer, nullable=False),
    Column("department", String(15), nullable=False),
)