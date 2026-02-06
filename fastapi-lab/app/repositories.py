from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate

class ITaskRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task_id: int, task_in: TaskCreate) -> Optional[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(
            id=self.current_id,
            **task_in.dict()
        )
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update(self, task_id: int, task_in: TaskCreate) -> Optional[Task]:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                # สร้าง Task object ใหม่พร้อมข้อมูลที่อัปเดต
                updated_task = Task(id=task_id, **task_in.model_dump())
                self.tasks[i] = updated_task
                return updated_task
        return None

    def delete(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
    

# app/repositories.py (เพิ่มต่อท้าย)
from sqlalchemy.orm import Session
from . import models_orm  # ต้องสร้าง SQLAlchemy Model แยก

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        return self.db.query(models_orm.Task).all()

    def create(self, task_in: TaskCreate) -> Task:
        db_task = models_orm.Task(**task_in.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def get_by_id(self, task_id: int):
        # ใช้ SQLAlchemy query หา Task ตาม id
        return self.db.query(models_orm.TaskORM).filter(models_orm.TaskORM.id == task_id).first()
    
    def update(self, task_id: int, task_in: TaskCreate):
        db_task = self.get_by_id(task_id)
        if db_task:
            # อัปเดตค่าจาก Pydantic model ลงใน ORM object
            for key, value in task_in.model_dump().items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete(self, task_id: int) -> bool:
        db_task = self.get_by_id(task_id)
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
            return True
        return False