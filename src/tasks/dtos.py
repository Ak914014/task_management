# data trasnfer object 
# for data vailidation file

from pydantic import BaseModel

class TaskSchema(BaseModel):
    title:str
    description:str
    is_completed:bool = False


# This for what i wanted to send the user so that if user have pasword and anyother data that i don't wanted to expose so that this will only give user id and title
class TaskResponseSchema(BaseModel):
    id:int
    title:str
    description:str
    is_completed:bool 
    