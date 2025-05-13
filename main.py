# main.py
from fastapi import FastAPI
from app.routes import liked

app = FastAPI()
app.include_router(liked.router, prefix="")

