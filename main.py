from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()
tasks = [
    {"id": 1, "title": "Learn Django", "done": False},
    {"id": 2, "title": "Get Hired", "done": False},
    {"id": 3, "title": "Feed Maku", "done": True}
]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/")
async def root_meta_data():
    return {
        "name": "To-do API", "version": 1.0, "endpoints": [
            "/health",
            "/tasks",
        ]
    }

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{id}")
async def get_tasks_by_id(id: int):
    for task in tasks:
        if task["id"] == id:
            return JSONResponse(
                status_code=200,
                content={
                    "task": task
                }
            )

    return JSONResponse(
        status_code=404,
        content={
            "error": f"Task {id} not found"
        }
    )

@app.post("/tasks")
async def create_task(title: str):
    if not title.strip():
        return JSONResponse(
            status_code=400,
            content={
                "error": "Title cannot be empty"
            }
        )

    if len(tasks) == 0:
        task_id = 1
    else:
        task_id = tasks[-1]["id"] + 1

    new_task = {"id": task_id, "title": title, "done": False}
    tasks.append(new_task)

    return JSONResponse(
        status_code=201,
        content={
            "new_task": new_task
        }
    )