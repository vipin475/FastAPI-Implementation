from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task API", 
    description="A simple task management API",
    version="1.0.0"
)

# Models
class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1, 
        max_length=100,
        description="The task title",
        examples=["Buy groceries"]
    )
    description: str | None = Field(
        default=None,
        description="Optional detailed description",
        examples=["Milk, bread, eggs"]
    )
    completed: bool = Field(
        default=False,
        description="Current status of the task"
    )
    
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
    """
    Create a new task with following properties
    - **title**: Required, 1-100 character
    - **description**: Optional details
    - **completed**: Optional, status of task
    """
    
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
def list_tasks(
    completed: bool | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = 10
):
    results = list(tasks_db.values())
    
    if completed is not None:
        results = [t for t in results if t.completed == completed]
    if search:
        results = [t for t in results if search.lower() in t.title.lower()]
    
    return results[skip: skip + limit]
    
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