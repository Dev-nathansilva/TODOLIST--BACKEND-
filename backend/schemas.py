from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pendente"
    priority: Optional[str] = "baixa"
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):  # 👈 novo schema para updates parciais
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None


class Task(TaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes  = True
