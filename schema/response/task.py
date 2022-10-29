from pydantic import BaseModel, Field
from schema import TaskStatus

class Task(BaseModel):
    """
    任務
    """
    id: int = Field(..., description="ID")
    name: str = Field(..., description="名稱")
    status: TaskStatus = Field(..., description="狀態")
