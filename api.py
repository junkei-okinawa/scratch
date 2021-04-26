from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://0.0.0.0",
    "http://127.0.0.1",
    "http://127.0.0.1:8601",
    "http://0.0.0.0:8601",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "root"

@app.get("/api/Hello/{id}")
def read_nom(id: int):
    return f"Hello api {id}"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}