from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/books/{book_id}")
def get_book(book_id: int):
    return {"book_id": book_id, "title": "Example Book"}

# Expose 'router' as 'api_router' for main.py
api_router = router

