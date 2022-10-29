from pydantic import BaseModel, Field

class CreateTask(BaseModel):
    """
    新增任務
    """
    name: str = Field(..., description="任務名稱")
