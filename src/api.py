from fastapi import FastAPI
from task import Task
from uvicorn import run

tasks: list[Task] = [
    Task(
        id="api-001",
        payload={
            "title": "Fix bug in production",
            "deadline": "yesterday",
            "priority": "maximum",
        },
    ),
    Task(
        id="api-002",
        payload={
            "title": "Buy pizza for the team",
            "deadline": "today",
            "priority": "high",
        },
    ),
    Task(
        id="api-003",
        payload={
            "title": "Talk with DeepSeek about AI future",
            "deadline": "in week",
            "priority": "low",
        },
    ),
    Task(
        id="api-004",
        payload={
            "title": "Finalize laboratory work №1",
            "deadline": "tomorrow",
            "priority": "medium",
        },
    ),
    Task(
        id="api-005",
        payload={
            "title": "Just sleep finally",
            "deadline": "in month",
            "priority": "skip",
        },
    ),
]

app = FastAPI()


@app.get("/")
async def root():
    return tasks


if __name__ == "__main__":
    run(app, host="localhost", port=8000)
