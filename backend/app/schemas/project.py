from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models.project import ProjectStatus
from app.schemas.user import UserResponse

# Base schema
class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    status: ProjectStatus = ProjectStatus.PLANNING

# Schema for creating a project
class ProjectCreate(ProjectBase):
    pass  # owner_id will be set from authenticated user

# Schema for updating a project
class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None

# Schema for project response
class ProjectResponse(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    owner: Optional[UserResponse] = None  # Include owner info if needed
    
    class Config:
        from_attributes = True