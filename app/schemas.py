from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from app.models import TaskStatus

# ─── Employee Schemas ───

class EmployeeBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    position: str = Field(min_length=2, max_length=100)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}

# ─── Task Schemas ───

class TaskBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=500)

class TaskCreate(TaskBase):
    employee_id: int

class TaskUpdate(BaseModel):
    status: TaskStatus

class TaskResponse(TaskBase):
    id: int
    status: TaskStatus
    employee_id: int
    created_at: datetime

    model_config = {"from_attributes": True}