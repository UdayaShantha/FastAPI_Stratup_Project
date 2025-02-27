from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel, Field
from uuid import UUID
from typing import List,Annotated
app = FastAPI()

class Book(BaseModel):
    id: UUID = Field(default_factory=UUID)
    author: str = Field(min_length=1, max_length=100)
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

@app.get("/read/books")
def read_books():
    return Books

Books=[]

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/save/books")
def save_books(book : Book):
    Books.append(book)
    return book

@app.put("/update/books/{id}")
def update_books(id : UUID, book : Book):
    counter=0
    for x in Books:
        counter=counter+1
        if x.id == id:
            # x.author = book.author
            # x.title = book.title
            # x.description = book.description
            # x.rating = book.rating
            Books[counter-1] = book
            return "Updated Book"
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

@app.delete("/delete/books/{id}")
def delete_books(id : UUID):
    counter=0
    for x in Books:
        counter=counter+1
        if x.id == id:
            del Books[counter-1]
            return "Book deleted successfully"
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )