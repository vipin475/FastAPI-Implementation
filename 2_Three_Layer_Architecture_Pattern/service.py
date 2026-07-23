import data
from models import Task, TaskCreate, TaskUpdate

class TaskNotFoundError(Exception):
    """Raised when a task doesn't exist"""
    pass

def get_all_tasks() -> list[Task]:
    return data.get_all()

def get_task(task_id: int) -> Task:
    task = data.get_one(task_id)
    if not task:
        raise TaskNotFoundError(f"Task {task_id} not found")
    return task

def create_task(task: TaskCreate) -> Task:
    # business logic should be here - check limits, send notification, etc
    return data.create(task)

def update_task(task_id: int, task_update: TaskUpdate) -> Task:
    get_task()
    
    updated = data.update(task_id, task_update)
    if not updated:
        raise TaskNotFoundError(f"Task {task_id} not found")
    return updated

def delete_task(task_id: int) -> None:
    # Verify task exists first
    get_task(task_id)
    data.delete(task_id)