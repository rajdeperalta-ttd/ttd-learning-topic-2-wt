from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory item store: {id: {"id": int, "name": str, "price": float}}
items = {}
next_id = 1


class Item(BaseModel):
    name: str
    price: float


# Task 1: Root and health endpoints
@app.get("/")
def read_root():
    # Return {"message": "Welcome to my API"}
    pass


@app.get("/health")
def health_check():
    # Return {"status": "ok"}
    pass


# Task 2 & 3: CRUD endpoints with optional name filter
@app.get("/items")
def get_items(name: str = None):
    # Return all items as a list
    # If 'name' query param is provided, filter items whose name contains it (case-insensitive)
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Return the item with the given item_id
    # Raise HTTPException(status_code=404) if not found
    pass


@app.post("/items")
def create_item(item: Item):
    # Add the item to the in-memory store with an auto-incremented ID
    # Return the created item including its ID
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Remove the item with the given item_id from the store
    # Return {"message": "Item deleted"}
    # Raise HTTPException(status_code=404) if not found
    pass
