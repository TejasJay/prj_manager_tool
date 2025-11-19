from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Base schema with common fields
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None

# Schema for creating a user
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

# Schema for updating a user
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)
    is_active: Optional[bool] = None

# Schema for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for user response (what we send back)
class UserResponse(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy model