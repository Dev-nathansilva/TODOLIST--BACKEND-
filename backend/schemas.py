from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class CategoryBase(BaseModel):
    name: str
    color: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pendente"
    priority: Optional[int] = 0
    due_date: Optional[datetime] = None
    category_id: Optional[uuid.UUID] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
