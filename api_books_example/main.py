from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 

# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs

app = FastAPI()                         # obtject to isntanciate the class

class Book(BaseModel):
    title: str
    author: str
    pages: int
    editorial: Optional[str]

@app.get("/")                           
def index():
    return{"message":"Hello World"}     # fastapi transform dictionary into json

@app.get("/books/{id}")
def show_books(id: int):
    return{"data": id}   

@app.post("/books")
def insert_book(book: Book):
    return{"message": f"Book: {book.title}"}