# data trasnfer object 
# for data vailidation file

from pydantic import BaseModel

class UserSchema(BaseModel):
    name : str
    username :str
    password : str
    email :str


# This for what i wanted to send the user so that if user have pasword and anyother data that i don't wanted to expose so that this will only give user id and title
class UserResponseSchema(BaseModel):
    name : str
    username :str
    email :str 
    