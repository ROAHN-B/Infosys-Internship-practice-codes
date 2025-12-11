from service import router as create_user
from fastapi import FastAPI

app=FastAPI()

app.include_router(create_user)