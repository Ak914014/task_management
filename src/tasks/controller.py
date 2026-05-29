# here we wrriten all logic how to create data recive data delete etc.. 
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel



def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], description = data["description"], is_completed= data["is_completed"] )

    db.add(new_task) ## this will add the new data 
    db.commit() ## when we commit that the data store in the table
    db.refresh(new_task)  ##fetches the latest data from the database and updates the Python object. and data like id and other default data


    return{"status":"Task created", "data":new_task }



def get_task(db:Session):
    tasks = db.query(TaskModel).all()
    return {"status":"all task", "data":tasks}