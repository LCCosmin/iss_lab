from sqlalchemy import create_engine, select, Row
from models.user import user
from models.user_data import user_data
from models.clocking_data import clocking_data
from models.tasks import tasks
from typing import Union, List
from task_generator import TaskGenerator
from enums.enums import EnumTask


class Controller:
    def __init__(self) -> None:
        self.db = create_engine('postgresql+psycopg2://postgres:c@localhost:5432/iss_lab').connect()
        
        self.task_generator = TaskGenerator(self.db)

    def try_login(self, username: str, password: str) -> Union[bool, str]:
        result = self.get_user_data(username, password)

        return(
            False
            if result is None
            else
            result.type
        )

    def get_user_data(self, username: str, password: str) -> Union[bool, Row]:
        query = (
            select(user)
            .select_from(user.join(user_data, user_data.c.user_id == user.c.id))
            .where(
                user.c.username == username,
                user_data.c.hashed_password == password,
            )
        )
        result = self.db.execute(query).fetchone()

        return(
            False
            if result is None
            else
            result
        )
        
    def get_active_employees(self) -> Row:
        query = (
            select(user)
            .select_from(user.join(clocking_data, clocking_data.c.employee_id == user.c.id))
            .where(
                clocking_data.c.is_active == True,
            )
        )
        result = self.db.execute(query).fetchall()

        return result
    
    def get_assigned_tasks(self, employee_id: str) -> List:
        query = (
            select(tasks)
            .select_from(tasks)
            .where(
                tasks.c.task_assignee == employee_id,
                tasks.c.status.in_(
                    [
                        EnumTask.READY_TO_TAKE.value,
                        EnumTask.IN_PROGRESS.value,
                        EnumTask.IN_REVIEW.value,
                    ]   
                )
            )
        )
        result = self.db.execute(query).fetchall()
        
        return result

    def get_uuid_by_name(self, username: str) -> str:
        query = (
            select(user.c.id)
            .select_from(user)
            .where(user.c.username == username)
        )
        result = self.db.execute(query).fetchone()
        
        return result.id

    def get_task_data(self, task_title: str) -> Row:
        query = (
            select(tasks)
            .select_from(tasks)
            .where(
                tasks.c.task_title == task_title,
                tasks.c.status.in_(
                    [
                        EnumTask.READY_TO_TAKE.value,
                        EnumTask.IN_PROGRESS.value,
                        EnumTask.IN_REVIEW.value,
                    ]   
                )
            )
        )
        result = self.db.execute(query).fetchone()
        
        return result

    def generate_new_task(
        self,
        task_name: str,
        task_description: str,
        task_story_points: int,
        assign_to_list: str,
        boss_name: str,
    ) -> None:
        id_employee = self.get_uuid_by_name(assign_to_list)
        id_boss = self.get_uuid_by_name(boss_name)
        
        self.task_generator.generate_new_task(
            task_name=task_name,
            task_description=task_description,
            task_story_points=task_story_points,
            employee_id=id_employee,
            boss_id=id_boss,
        )

    def move_task_next_step(self, task_id: str, task_status: str):
        match task_status:
            case EnumTask.READY_TO_TAKE.value:
                task_status = EnumTask.IN_PROGRESS.value
            case EnumTask.IN_PROGRESS.value:
                task_status = EnumTask.IN_REVIEW.value
            case EnumTask.IN_REVIEW.value:
                task_status = EnumTask.DONE.value
        
        self.task_generator.update_task(task_id=task_id, task_status=task_status)
        
    def move_task_prev_step(self, task_id: str, task_status: str):
        match task_status:
            case EnumTask.IN_REVIEW.value:
                task_status = EnumTask.IN_PROGRESS.value
            case EnumTask.IN_PROGRESS.value:
                task_status = EnumTask.READY_TO_TAKE.value
        
        self.task_generator.update_task(task_id=task_id, task_status=task_status)
