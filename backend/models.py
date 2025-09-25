from enum import Enum
from sqlalchemy import Column, String, Enum as SQLAEnum, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from database import Base


class TaskStatus(str, Enum):
    pendente = "pendente"
    progresso = "em progresso"
    finalizado = "finalizado"


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    color = Column(String(7))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(SQLAEnum(TaskStatus, name="task_status"), default=TaskStatus.pendente)
    priority = Column(Integer, default=0)
    due_date = Column(TIMESTAMP(timezone=True))
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id", ondelete="SET NULL"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
