from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))

    task = relationship("Task", back_populates="users")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    description = Column(String, index=True)
    ready = Column(Boolean, default=False)

    users = relationship("User", back_populates="task")
