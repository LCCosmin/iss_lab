from enum import Enum


class EnumUser(Enum):
    BOSS = 'BOSS'
    EMPLOYEE = 'EMPLOYEE'
  

class EnumDepartment(Enum):
    FINANCE = 'FINANCE'
    KPI = 'KPI'
    ROBOTICS = 'ROBOTICS'
    AUTOMATION = 'AUTOMATION'


class EnumTask(Enum):
    READY_TO_TAKE = 'READY TO TAKE'
    IN_PROGRESS = 'IN PROGRESS'
    IN_REVIEW = 'IN REVIEW'
    DONE = 'DONE'


class EnumClock(Enum):
    CLOCK_IN = 'CLOCK IN'
    CLOCK_OUT = 'CLOCK OUT'
