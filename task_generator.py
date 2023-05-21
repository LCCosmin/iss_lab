from uuid import uuid1
from enums.enums import EnumTask
from sqlalchemy import insert, Connection, update
from models.tasks import tasks


class TaskGenerator:
    def __init__(self, db: Connection):
        self.db = db

    def generate_new_task(
        self,
        task_name: str,
        task_description: str,
        task_story_points: int,
        employee_id: str,
        boss_id: str,
    ) -> None:
        task_id = uuid1()
        query = (
            insert(tasks)
            .values(
                id=task_id,
                task_title=task_name,
                task_description=task_description,
                story_points=task_story_points,
                task_creator=boss_id,
                task_assignee=employee_id,
                status=EnumTask.READY_TO_TAKE.value
            )
        )
        
        self.db.execute(query)
        self.db.commit()

    def update_task(self, task_id: str, task_status: str) -> None:
        query = (
            update(tasks)
            .where(tasks.c.id == task_id)
            .values(status=task_status)
        )
        
        self.db.execute(query)
        self.db.commit()
