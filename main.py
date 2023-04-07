import os
from fastapi import FastAPI
from sunbeam import List, ListItem

app = FastAPI()

DETA_API_KEY = os.getenv("DETA_API_KEY")


@app.get("/")
async def root():
    return List(items=[ListItem(title="detail", actions=[])]).dict()


@app.get("/list")
async def list():
    return {
        "type": "detail",
        "text": "Detail, detail, detail",
    }


@app.get("/hello")
async def hello(name: str):
    return {
        "type": "detail",
        "text": f"Hello {name}",
    }
