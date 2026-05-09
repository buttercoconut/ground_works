"""Task API endpoints.

Placeholder for task related operations.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.models.task import Task, TaskCreate, TaskRead
from backend.services.task_service import TaskService

router = APIRouter()

# Dependency to get DB session

def get_db():
    from backend.main import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.create_task(task_in)

@router.get("/", response_model=List[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.list_tasks()

# Additional endpoints can be added similarly
