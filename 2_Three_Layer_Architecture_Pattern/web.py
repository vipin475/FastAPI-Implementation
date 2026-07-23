import service
from fastapi import APIRouter, HTTPException, status
from models import TaskUpdate, Task, TaskCreate
from service import TaskNotFoundError

router = APIRouter(prefix="/task", tags=["tasks"])

@router.get("/", response_model=list[Task])
def list_tasks():
    return service.get_all_tasks()
    
@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    try:
        return service.get_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    
@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    return service.create_task(task)

@router.patch("/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    try:
        return service.update_task(task_id, task_update)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    try:
        service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")