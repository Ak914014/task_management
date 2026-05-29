from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes


app = FastAPI()
app.include_router(task_routes)

# pip freeze > requirement.txt      ----to get the all the dependencies in the project