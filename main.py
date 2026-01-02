from fastapi import FastAPI, HTTPException, Depends
import services, model, schemas
from db import get_db, engine
from routes import user_routs, book_routs
from sqlalchemy.orm import Session
from auth import get_current_user

app = FastAPI()
model.Base.metadata.create_all(bind=engine)
app.include_router(user_routs.router)
app.include_router(book_routs.router)

# @app.get("/books/", response_model=list[schemas.BookResponse])
# def get_books(db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
#     return services.get_books(db)

# @app.get("/books/paginated/", response_model=list[schemas.BookResponse])
# def get_books_paginated(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
#     return services.get_books_with_pagination(db, skip=skip, limit=limit)

# @app.post("/books/", response_model=schemas.BookResponse)
# def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
#     # Validate the book data then store it to the database
#     # return {"data": services.create_book(db, book), "message": "Book created successfully"}
#     return services.create_book(db, book)

# @app.put("/books/{id}", response_model=schemas.BookResponse)
# def update_book(id: int, book: schemas.BookCreate, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
#     existing_book = services.update_book(db, id, book)
#     if not existing_book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return existing_book

# @app.delete("/books/{id}", response_model=schemas.BookResponse)
# def delete_book(id: int, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
#     query_book = services.delete_book(db, id)
#     if not query_book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return query_book
#     services.delete_book(db, id)
