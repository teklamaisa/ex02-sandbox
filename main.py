from enum import Enum

from fastapi import FastAPI

from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None    

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.delete("/")
async def death():
    return {"message": "Deleted root :)"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.post("/items/")
async def create_item(item: Item):
    return item