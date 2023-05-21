from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_data = Table(
    "user_data",
    Base.metadata,
    Column("id", String(255), nullable=False, primary_key=True),
    Column("user_id", String(255), nullable=False),
    Column("hashed_password", String(255), nullable=False),
)