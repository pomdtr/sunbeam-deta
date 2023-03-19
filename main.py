from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "type": "list",
        "items": [
            {
                "title": "First item",
                "actions": [{"type": "http", "url": "./first-item"}],
            },
            {
                "title": "Second item",
                "actions": [{"type": "http", "url": "./second-item"}],
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
