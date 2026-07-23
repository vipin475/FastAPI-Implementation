from datetime import datetime
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    """What the client sends to create a task"""

    title: str = Field(
        min_length=1, 
        max_length=100,
        description="The task title",
        examples=["Buy groceries"]
    )
    description: str | None = Field(
        default=None,
        description="Optional detailed description",
        examples=["Milk, bread, eggs"]
    )

    
class Task(BaseModel):
    """The complete task representation"""
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    
class TaskUpdate(BaseModel):
    """Fields that can be updated (all optional)"""
    title: str | None = None
    description: str | None = None
    completed: bool | None = None