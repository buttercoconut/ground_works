"""Pydantic models for the boring task API.

These schemas are used for request validation and response serialization.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: str = Field("pending", regex="^(pending|in_progress|completed|failed)$")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[str] = Field(None, regex="^(pending|in_progress|completed|failed)$")

class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
