from fastapi import APIRouter, HTTPException
from typing import List
from models.book import Book

router = APIRouter()

# Sample books database (replace with actual database queries)
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

@router.get("/api/v1/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

