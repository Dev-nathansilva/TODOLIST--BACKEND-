from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    color = Column(String(7))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

     # Relacionamento
    tasks = relationship("Task", back_populates="category", cascade="all, delete")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="pendente")
    priority = Column(Integer, default=0)
    due_date = Column(TIMESTAMP(timezone=True))
    category_id = Column(UUID(as_uuid=True),ForeignKey("categories.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relacionamento inverso
    category = relationship("Category", back_populates="tasks")