from fastapi import FastAPI, Depends
from typing import List
from .models import Task, TaskCreate
from .repositories import InMemoryTaskRepository, SqlTaskRepository
from .services import TaskService
from .import models_orm
from .database import SessionLocal, engine 
from sqlalchemy.orm import Session 
from fastapi import HTTPException, Response, status


models_orm.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Singleton Repository Instance
task_repo = InMemoryTaskRepository()

def get_db():
    db = SessionLocal()  # เปิดประตูบ้านของจริงแล้ว
    try:
        yield db
    finally:
        db.close()  # ปิดประตูทุกครั้งหลังใช้งานเสร็จ

# ใหม่ (ใช้ SQL):
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.get_task(task_id)
    if task is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate, 
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_in: TaskCreate, service: TaskService = Depends(get_task_service)):
    updated_task = service.update_task(task_id, task_in)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)