from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import session

from src.tasks.models import TaskModel

from fastapi import HTTPException

def create_task(body:TaskSchema,db:session):

    data = body.model_dump()

    new_task = TaskModel(
        title = data["title"],
        derscription = data["description"],
        is_completed = data["is_completed"]
    )
    db.add(new_task)
    db.commit()
    db.refresh()
    return{"Status":"Task ceated successfully", "Data":new_task}



def get_all_tasks(db:session):
    task = db.query(TaskModel).all()
    return {"Status":"All task", "Data":task}

def get_one_tasks(task_id:int,db:session):
    one_task = db.query(TaskModel).get(task_id)

    if not one_task:
        return HTTPException(404,detail="Task id is incorrect")

    return {"Status":"Task Fatched successfully", "Data":one_task}



def update_task(task_id:int,db:session):
    one_task = db.query(TaskSchema).get(task_id)

    if not one_task:
        return HTTPException(404,detail="Task id is incorrect")

    body = body.model_dump()
    for field,value in body.items():
        setattr(one_task,field,value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return{
        "Status":"Update task successfully",
        "Data":one_task
    }



def delete_task(task_id:int,db:session):
    one_task = db.query(TaskSchema).get(task_id)

    if not one_task:
        return HTTPException(404,detail="Task id is incorrect")

    db.delete(one_task)
    db.commit()

    return {
        "Status":"Task deleted successfully",
        "Data":one_task
    }



def delete_all_task(db:session):
    tasks = db.query(TaskModel).all()

    for task in tasks:
        db.delete(task)

    db.commit()
    return{
         "Status":"All Task deleted successfully",
    }
