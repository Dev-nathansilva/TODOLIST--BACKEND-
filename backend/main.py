from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db
from typing import List
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tasks
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    task = crud.get_task(db, str(task_id))
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: uuid.UUID, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, str(task_id), task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    return crud.delete_task(db, str(task_id))