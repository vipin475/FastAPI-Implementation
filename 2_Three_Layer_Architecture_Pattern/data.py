from datetime import datetime
from models import TaskUpdate, Task, TaskCreate

# fake database
_tasks: dict[int, Task] = {}
_id_counter = 1

def get_all() -> list[Task]:
    return list(_tasks.values())

def get_one(task_id: int) -> Task:
    return _tasks.get(task_id)

def create(task: TaskCreate) -> Task:
    global _id_counter
    new_task = Task(
        id=_id_counter,
        title=task.title,
        description=task.description,
        completed=False,
        created_at=datetime.now(),
    )
    _tasks[_id_counter] = new_task
    _id_counter += 1
    return new_task

def update(task_id: int, task_update: TaskUpdate) -> Task | None:
    if task_id not in _tasks:
        return None
    
    existing = _tasks[task_id]
    update_data = task_update.model_dump(exclude_unset=True)
    updated = Task(
        id=existing.id,
        title=update_data.get("title", existing.title),
        description=update_data.get("description", existing.description),
        completed=update_data.get("completed", existing.completed),
        created_at=existing.created_at,
    )
    _tasks[task_id] = updated
    return updated

def delete(task_id: int) -> bool:
    if task_id in _tasks:
        del _tasks[task_id]
        return True
    return False