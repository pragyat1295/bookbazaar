from sqlalchemy.orm import Session
from schemas import BookCreate, BookResponse
from services.books_services import create_book, update_book
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from auth import get_current_user, require_admin_or_super_admin
from model import User, Book

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=BookResponse)
def create_book_route(book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_book(db, book, user_id=current_user.id)

@router.get("/", response_model=list[BookResponse])
def get_books_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Book).all()

@router.patch("/{id}", response_model=BookResponse)
def update_book_route(id: int, book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(require_admin_or_super_admin)):
    existing_book = update_book(db, id, book)
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return existing_book