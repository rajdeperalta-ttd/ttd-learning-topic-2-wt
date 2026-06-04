# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework by creating endpoints that handle HTTP methods, path parameters, query parameters, and request bodies with automatic data validation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application and create a simple root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import `FastAPI` from the `fastapi` module and create an `app` instance.
- Define a `GET` endpoint at `/` that returns a JSON response: `{"message": "Welcome to my API"}`.
- Define a `GET` endpoint at `/health` that returns `{"status": "ok"}`.

### 🛠️ Build a CRUD Endpoint for Items

#### Description
Create endpoints to manage a collection of items stored in memory using a Python dictionary.

#### Requirements
Completed program should:

- Define a `GET` endpoint at `/items` that returns all items as a list.
- Define a `GET` endpoint at `/items/{item_id}` that returns a single item by its integer ID, or raises an `HTTPException` with status code `404` if the item is not found.
- Define a `POST` endpoint at `/items` that accepts a JSON body with `name` (str) and `price` (float) fields, adds the item to the in-memory store, and returns the created item with its assigned ID.
- Define a `DELETE` endpoint at `/items/{item_id}` that removes an item by ID and returns `{"message": "Item deleted"}`, or raises a `404` if not found.
- Example usage:
  ```
  POST /items   body: {"name": "Pencil", "price": 0.99}
  GET  /items/1 → {"id": 1, "name": "Pencil", "price": 0.99}
  ```

### 🛠️ Add Query Parameter Filtering

#### Description
Extend the `GET /items` endpoint to support optional query parameter filtering by item name.

#### Requirements
Completed program should:

- Accept an optional query parameter `name` (str) on `GET /items`.
- When `name` is provided, return only items whose name contains the given string (case-insensitive).
- When `name` is not provided, return all items as before.
- Example:
  ```
  GET /items?name=pen → returns all items with "pen" in the name
  GET /items          → returns all items
  ```
