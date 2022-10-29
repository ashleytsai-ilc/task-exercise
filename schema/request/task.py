from pydantic import BaseModel, Field
from schema import TaskStatus

class CreateTask(BaseModel):
    """
    新增任務
    """
    name: str = Field(..., description="任務名稱")

class UpdateTask(BaseModel):
    """
    更新任務
    """
    id: int = Field(..., description="ID")
    name: str = Field(..., description="名稱")
    status: TaskStatus = Field(..., description="狀態")
