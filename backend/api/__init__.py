"""API router for the Ground Works backend.

All endpoints are defined in this module and then included in the main
application via :func:`app.include_router`.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..models.task import TaskCreate, TaskRead, TaskUpdate, Task
from ..services.task_service import TaskService

router = APIRouter()

# Dependency to get a TaskService instance
async def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)

# Create a new boring task
@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return await service.create_task(task_in)

# Retrieve a task by ID
@router.get("/tasks/{task_id}", response_model=TaskRead)
async def read_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    task = await service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task
@router.put("/tasks/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    task_in: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    task = await service.update_task(task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Delete a task
@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    success = await service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None

# List tasks with optional pagination
@router.get("/tasks", response_model=list[TaskRead])
async def list_tasks(
    skip: int = 0,
    limit: int = 10,
    service: TaskService = Depends(get_task_service),
):
    return await service.list_tasks(skip=skip, limit=limit)
