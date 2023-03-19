import os
from fastapi import FastAPI

app = FastAPI()

DETA_API_KEY = os.getenv("DETA_API_KEY")


@app.get("/")
async def root():
    return {
        "type": "list",
        "items": [
            {
                "title": "First item",
                "actions": [{"type": "http", "url": "./first-item", "headers": {
                    "x-api-key": DETA_API_KEY,
                }}],
            },
            {
                "title": "Second item",
                "actions": [{"type": "http", "url": "./second-item", "headers": {
                    "x-api-key": DETA_API_KEY,
                }}],
            },
        ],
    }


@app.get("/first-item")
async def first_item():
    return {
        "type": "detail",
        "text": "This is the first item",
    }


@app.get("/second-item")
async def second_item():
    return {
        "type": "detail",
        "text": "This is the second item",
    }
