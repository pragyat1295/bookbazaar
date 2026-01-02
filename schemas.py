from pydantic import BaseModel
from typing import List
from user_enum import UserType
    
# ----------------------- Book Schemas -----------------------

class BookBase(BaseModel):
    title: str
    description: str
    author: str
    year_published: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
        # orm_mode = True 
        # for the older versions

# ----------------------- User Schemas -----------------------

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str
    user_type: UserType

class UserResponse(UserBase):
    id: int
    user_type: UserType
    books: List[BookResponse] = []

    class Config:
        from_attributes = True
        # orm_mode = True 
        # for the older versions
