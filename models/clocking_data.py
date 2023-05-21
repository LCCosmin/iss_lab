from sqlalchemy import Table, Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

clocking_data = Table(
    "clocking_data",
    Base.metadata,
    Column("id", String(255), nullable=False, primary_key=True),
    Column("employee_id", String(255), nullable=False),
    Column("date_clock_in", DateTime, nullable=False),
    Column("date_clock_out", DateTime, nullable=False),
    Column("time_clock_in", DateTime, nullable=False),
    Column("time_clock_out", DateTime, nullable=False),
    Column("is_active", Boolean, nullable=False),
)
