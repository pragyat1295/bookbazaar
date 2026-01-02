from model import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

### Books Services

### Explanation of ** operator:
# the ** operator in Python is used to unpack a dictionary into keyword arguments when calling a function or creating an object.
# Pydantic input
# book = BookCreate(title="1984", author="Orwell", price=9.99)
# data = book.model_dump() # -> {'title': '1984','author':'Orwell','price':9.99}
# new_book = Book(**data) # -> Book(title='1984', author='Orwell', price=9.99)

def create_book(db: Session, book: BookCreate, user_id: int):
    new_Book = Book(**book.model_dump(), user_id=user_id) # the ** explanation is above. 
    db.add(new_Book)
    db.commit()
    db.refresh(new_Book)
    return new_Book

def get_books(db: Session):
    return db.query(Book).all()

def get_books_with_pagination(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def update_book(db: Session, id: int, book: BookCreate):
    existing_book = db.query(Book).filter(Book.id == id).first()
    if existing_book:
        for attr, value in book.model_dump().items():
            setattr(existing_book, attr, value)

        db.commit()
        db.refresh(existing_book)
    return existing_book

def delete_book(db: Session, id: int):
    existing_book = db.query(Book).filter(Book.id == id).first()

    if existing_book:
        db.delete(existing_book)
        db.commit()
        db.refresh(existing_book)
    return existing_book

def delete_book(db: Session, id: int):
    existing_book = db.query(Book).filter(Book.id == id).first()

    if existing_book:
        db.delete(existing_book)
        db.commit()
        # db.refresh(existing_book)
    return existing_book