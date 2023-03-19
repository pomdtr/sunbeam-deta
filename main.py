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
                "title": "Detail",
                "actions": [
                    {
                        "type": "http",
                        "url": "./list",
                        "headers": {
                            "x-api-key": DETA_API_KEY,
                        } if DETA_API_KEY else {},
                    }
                ],
            },
            {
                "title": "Form",
                "actions": [
                    {
                        "type": "http",
                        "url": "./hello?name=${input:name}",
                        "headers": {
                            "x-api-key": DETA_API_KEY,
                        } if DETA_API_KEY else {},
                        "inputs": [
                            {
                                "name": "name",
                                "type": "textfield",
                                "title": "Name",
                            }
                        ]
                    }
                ],
            },
        ],
    }


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
