from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db
from typing import List
import uuid

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Categories
@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

@app.delete("/categories/{category_id}")
def delete_category(category_id: uuid.UUID, db: Session = Depends(get_db)):
    crud.delete_category(db, str(category_id))
    return {"ok": True}

# Tasks
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: uuid.UUID, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, str(task_id), task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    crud.delete_task(db, str(task_id))
    return {"ok": True}
