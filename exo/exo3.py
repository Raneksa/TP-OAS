from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse   

app = FastAPI()
@app.get("/task")
def get_task():
    task_data = {
        "id": int,
        "title": "Faire les courses",
        "completed": False
    }
    return JSONResponse(content=task_data, status_code=200)

@app.post("/tasks")
def create_task(task: dict):
    if "title" not in task or not isinstance(task["title"], str):
        return JSONResponse(content={"error": "Task not found"}, status_code=400)
    
    new_task = {
        "id": 2,
        "title": task["title"],
        "completed": False
    }
    return JSONResponse(content=new_task, status_code=201)

@app.GET("/tasks/{id}")
def get_task_by_id(id: int):
    task_data = {
        "id": 1,
        "title": "Faire les courses",
        "completed": False
    }
    return JSONResponse(content=task_data, status_code=200)

@app.delete("/tasks/{id}")
def delete_task(id: int):
    return JSONResponse(content={"message": f"Task deleted"}, status_code=200)

@app.delete("/tasks")
def delete_all_tasks():
    return JSONResponse(content={"message": f"All tasks deleted : "}, status_code=200)