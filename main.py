from fastapi import FastAPI

app = FastAPI()

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

