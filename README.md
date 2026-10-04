Here’s a clean, beginner-friendly `README.md` for your FastAPI To-do API. It documents the endpoints, setup, examples, and current behavior of your implementation.

 README.md

# To-do API

 A simple RESTful To-do API built with **FastAPI** and **Python**.

 This project provides endpoints for creating, reading, updating, and deleting tasks. Tasks are currently stored in an in-memory Python list, so the data will be reset whenever the application restarts.

 ## Features

 - Health check endpoint
- API metadata endpoint
- Get all tasks
- Get a task by ID
- Create a new task
- Update an existing task
- Delete a task
- Basic validation for task titles
- JSON responses with appropriate HTTP status codes

 ## Requirements

 - Python 3.9+
- FastAPI
- Uvicorn

 ## Installation

 Clone the repository and navigate into the project directory:

```
git clone <your-repository-url>
cd <your-project-directory>
```

 Create and activate a virtual environment:

 ### Windows

```
python -m venv venv
venv\Scripts\activate
```

 ### macOS/Linux

```
python3 -m venv venv
source venv/bin/activate
```

 Install the dependencies:

```
pip install fastapi uvicorn
```

 ## Running the API

 Assuming your FastAPI application is saved as `main.py`, start the development server with:

```
uvicorn main:app --reload
```

 The API will be available at:

```
http://127.0.0.1:8000
```

 ## API Documentation

 FastAPI automatically generates interactive API documentation.

 ### Swagger UI

```
http://127.0.0.1:8000/docs
```

 ### ReDoc

```
http://127.0.0.1:8000/redoc
```

 ## Endpoints

 | Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Check if the API is running |
| GET | `/` | Get API metadata |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task |

---

 ## `GET /health`

 Checks whether the API is running.

 ### Response

```
{
  "status": "ok"
}
```

---

 ## `GET /`

 Returns basic information about the API.

 ### Response

```
{
  "name": "To-do API",
  "version": 1.0,
  "endpoints": [
    "/health",
    "/tasks"
  ]
}
```

---

 ## `GET /tasks`

 Returns all tasks.

 ### Example response

```
[
  {
    "id": 1,
    "title": "Learn Django",
    "done": false
  },
  {
    "id": 2,
    "title": "Get Hired",
    "done": false
  },
  {
    "id": 3,
    "title": "Feed Maku",
    "done": true
  }
]
```

---

 ## `GET /tasks/{id}`

 Returns a specific task by its ID.

 ### Example

```
GET /tasks/1
```

 ### Successful response

```
{
  "task": {
    "id": 1,
    "title": "Learn Django",
    "done": false
  }
}
```

 ### Not found response

 If the task does not exist:

```
{
  "error": "Task 99 not found"
}
```

 Status code:

```
404 Not Found
```

---

 ## `POST /tasks`

 Creates a new task.

 The current implementation accepts `title` as a query parameter.

 ### Example request

```
POST /tasks?title=Learn%20FastAPI
```

 ### Successful response

```
{
  "new_task": {
    "id": 4,
    "title": "Learn FastAPI",
    "done": false
  }
}
```

 Status code:

```
201 Created
```

 ### Empty title

 An empty or whitespace-only title is rejected.

 Example:

```
POST /tasks?title=
```

 Response:

```
{
  "error": "Title cannot be empty"
}
```

 Status code:

```
400 Bad Request
```

---

 ## `PUT /tasks/{id}`

 Updates an existing task's title and completion status.

 The current implementation accepts `title` and `done` as query parameters.

 ### Example request

```
PUT /tasks/1?title=Learn%20FastAPI&done=true
```

 ### Successful response

```
{
  "updated_task": {
    "id": 1,
    "title": "Learn FastAPI",
    "done": true
  }
}
```

 Status code:

```
200 OK
```

 ### Task not found

```
{
  "error": "Task not found"
}
```

 Status code:

```
404 Not Found
```

---

 ## `DELETE /tasks/{id}`

 Deletes a task by its ID.

 ### Example

```
DELETE /tasks/1
```

 Successful deletion returns:

```
204 No Content
```

 If the task does not exist:

```
{
  "error": "Task does not exist"
}
```

 Status code:

```
404 Not Found
```

 ## Example with cURL

 ### Check the API

```
curl http://127.0.0.1:8000/health
```

 ### Get all tasks

```
curl http://127.0.0.1:8000/tasks
```

 ### Get one task

```
curl http://127.0.0.1:8000/tasks/1
```

 ### Create a task

```
curl -X POST "http://127.0.0.1:8000/tasks?title=Learn%20FastAPI"
```

 ### Update a task

```
curl -X PUT "http://127.0.0.1:8000/tasks/1?title=Learn%20FastAPI&done=true"
```

 ### Delete a task

```
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

 ## Project Structure

 A simple project structure could look like this:

```
todo-api/
├── main.py
├── README.md
└── requirements.txt
```

 Example `requirements.txt`:

```
fastapi
uvicorn
```

 Install the requirements with:

```
pip install -r requirements.txt
```

 ## Data Storage

 This project currently uses an in-memory Python list:

```
tasks = [
    {"id": 1, "title": "Learn Django", "done": False},
    {"id": 2, "title": "Get Hired", "done": False},
    {"id": 3, "title": "Feed Maku", "done": True}
]
```

 Because there is no database, all changes are temporary.

 If the application is restarted:

 - Newly created tasks are lost.
- Deleted tasks return.
- Updated tasks return to their original values.
