from sqlalchemy.orm import Session
from model import User
from schemas import UserCreate, UserResponse
from services.user_services import create_user, login_user
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def user_login(email: str, password: str, db: Session = Depends(get_db)):
    token = login_user(db, email, password)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(User).all()

@router.post("/logout")
def user_logout(current_user: User = Depends(get_current_user)):
    return {"message": "User logged out successfully"}