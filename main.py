from fastapi import FastAPI
from src.utils.db import base,engine
from src.tasks.models import TaskModel
from src.tasks.models import task_routes
from fastapi.middleware.cors import CORSMiddleware

# base.metadata.create_all(engine)

app = FastAPI(title="Task Management System")

app.include_router(task_routes)