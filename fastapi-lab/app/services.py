from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_task(self, task_id: int):
        # เรียกใช้ repo เพื่อหาข้อมูล
        return self.repo.get_by_id(task_id)

    def create_task(self, task_in: TaskCreate):
        # Business logic could go here
        return self.repo.create(task_in)
    
    def update_task(self, task_id: int, task_in: TaskCreate):
        return self.repo.update(task_id, task_in)

    def delete_task(self, task_id: int):
        return self.repo.delete(task_id)