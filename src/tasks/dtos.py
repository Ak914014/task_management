# data trasnfer object 
# for data vailidation file

from pydantic import BaseModel

class TaskSchema(BaseModel):
    title:str
    description:str
    is_completed:bool = False