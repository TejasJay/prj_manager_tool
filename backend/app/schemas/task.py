from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus, TaskPriority
from app.schemas.user import UserResponse
from app.schemas.project import ProjectResponse

# Base schema
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None

# Schema for creating a task
class TaskCreate(TaskBase):
    project_id: int
    assignee_id: Optional[int] = None

# Schema for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    project_id: Optional[int] = None
    assignee_id: Optional[int] = None
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = None

# Schema for task response
class TaskResponse(TaskBase):
    id: int
    project_id: int
    assignee_id: Optional[int] = None
    is_completed: bool
    created_at: datetime
    updated_at: datetime
    project: Optional[ProjectResponse] = None  # Include project info if needed
    assignee: Optional[UserResponse] = None  # Include assignee info if needed
    
    class Config:
        from_attributes = True