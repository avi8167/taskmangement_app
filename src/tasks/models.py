from sqlalchemy import Column,Integer,String,Boolean

from src.utils.db import base

class TaskModel(base):

    __tablename__= "user_task1"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean,defult = False)
