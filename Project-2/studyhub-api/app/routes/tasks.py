from fastapi import APIRouter, status, HTTPException
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# temporary database
tasks = []
next_id = 1

# GET all tasks
@router.get("/tasks", response_model=list[TaskResponse], status_code=status.HTTP_200_OK, summary="Get all tasks")
def get_tasks():
    return tasks

# POST all task
@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, summary="Create a new task")
def create_tasks(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    next_id += 1

    return new_task

# GET single task
@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK, summary="Get a single task")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Task not found"
    )

# PUT update task
@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK, summary="Update a task")
def update_task(task_id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

# DELETE task
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a task")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )