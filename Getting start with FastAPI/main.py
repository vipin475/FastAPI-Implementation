from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from pydantic import BaseModel, Field

app = FastAPI(title="Task API", version="1.0.0")

# Models
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    completed: bool = False
    
class Task(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    

# Fake database
tasks_db: dict[int, Task] = {}
task_id_counter = 1

# endpoints
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=datetime.now(),
    )
    tasks_db[task_id_counter] = new_task
    task_id_counter += 1
    return new_task

@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks_db.values())
    
    
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    if task_id not in tasks_db:
            raise HTTPException(status_code=404, detail="Task not found")
        
    existing = tasks_db[task_id]
    updated_data = task_update.model_dump(exclude_unset=True)
    updated_task = existing.model_copy(update=updated_data)
    tasks_db[task_id] = update_task
    return updated_task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}