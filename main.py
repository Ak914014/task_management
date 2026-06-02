from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.user.router import user_routes

app = FastAPI()
app.include_router(task_routes)
app.include_router(user_routes)

# pip freeze > requirement.txt      ----to get the all the dependencies in the project