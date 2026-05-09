"""Service layer for boring tasks.

The service encapsulates all business logic and database interactions.
It is intentionally asynchronous to allow future integration with async
ORMs or external services.
"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.task import Task
from ..api.boring import TaskCreate, TaskRead, TaskUpdate

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    async def create_task(self, task_in: TaskCreate) -> TaskRead:
        task = Task(**task_in.dict())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return TaskRead.from_orm(task)

    async def get_task(self, task_id: int) -> Optional[TaskRead]:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            return TaskRead.from_orm(task)
        return None

    async def update_task(self, task_id: int, task_in: TaskUpdate) -> Optional[TaskRead]:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        for field, value in task_in.dict(exclude_unset=True).items():
            setattr(task, field, value)
        self.db.commit()
        self.db.refresh(task)
        return TaskRead.from_orm(task)

    async def delete_task(self, task_id: int) -> bool:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        self.db.delete(task)
        self.db.commit()
        return True

    async def list_tasks(self, skip: int = 0, limit: int = 10) -> List[TaskRead]:
        tasks = self.db.query(Task).offset(skip).limit(limit).all()
        return [TaskRead.from_orm(t) for t in tasks]
