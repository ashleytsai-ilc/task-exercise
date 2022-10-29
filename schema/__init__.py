from enum import IntEnum

class TaskStatus(IntEnum):
    """
    任務狀態
    0: 未完成
    1: 已完成
    """
    INCOMPLETE = 0
    COMPLETE = 1
