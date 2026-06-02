# here we wrriten all logic how to create data recive data delete etc.. 
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException


def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], description = data["description"], is_completed= data["is_completed"] )

    db.add(new_task) ## this will add the new data 
    db.commit() ## when we commit that the data store in the table
    db.refresh(new_task)  ##fetches the latest data from the database and updates the Python object. and data like id and other default data


    return new_task 



def get_task(db:Session):
    tasks = db.query(TaskModel).all()
    return tasks



def get_one_task(task_id:int,db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail = "task Id is incorrect")
    
   
    return one_task




def update_task(body:TaskSchema, task_id:int, db:Session):

    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail = "task Id is incorrect")
    

    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed
#  this is not good way to updated the data if user have many line of data than user can't updated by this way or user only wanted to 
#  to pass a sinlge value change than also this is not the good way now bellow i have the better way to 

    body = body.model_dump()
    for field, value in body.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)


    return one_task
    
   

def delete_task(task_id:int, db:Session):
    
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail = "task Id is incorrect")
    

    db.delete(one_task)
    db.commit()

    return None