from fastapi import FastAPI
from typing import List
from datetime import datetime

from src.task.model import Task
from src.task.enums import PriorityEnum, StatusEnum

tasks: List[Task] = [
    Task(
        id=1,
        description="Fix bug in production - critical issue affecting users",
        priority=PriorityEnum.maximum,  # 4
        status=StatusEnum.pending,       # 0
        created_at=datetime(2026, 4, 2, 10, 30, 0)
    ),
    Task(
        id=2,
        description="Buy pizza for the team",
        priority=PriorityEnum.high,       # 3
        status=StatusEnum.pending,        # 0
        created_at=datetime(2026, 4, 3, 9, 0, 0)
    ),
    Task(
        id=3,
        description="Talk with DeepSeek about AI future",
        priority=PriorityEnum.low,        # 1
        status=StatusEnum.in_progress,    # 1
        created_at=datetime(2026, 4, 1, 15, 20, 0)
    ),
    Task(
        id=4,
        description="Finalize laboratory work №2",
        priority=PriorityEnum.medium,     # 2
        status=StatusEnum.pending,        # 0
        created_at=datetime(2026, 4, 3, 8, 0, 0)
    ),
    Task(
        id=5,
        description="Just sleep finally",
        priority=PriorityEnum.minimum,    # 0
        status=StatusEnum.completed,      # 2
        created_at=datetime(2026, 3, 30, 23, 0, 0)
    ),
    Task(
        id=6,
        description="Write comprehensive tests",
        priority=PriorityEnum.high,       # 3
        status=StatusEnum.pending,        # 0
        created_at=datetime(2026, 4, 3, 11, 0, 0)
    ),
]

app = FastAPI()


@app.get("/", response_model=List[dict])
async def root() -> List[dict]:
    """
    Эндпоинт для получения всех задач из API.

    Returns:
        list[dict]: Список задач в виде словарей.
    """
    return [task.to_dict() for task in tasks]
