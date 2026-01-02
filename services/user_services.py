from sqlalchemy.orm import Session
from model import User
from schemas import UserCreate
from fastapi import HTTPException
from auth import hash_password, create_access_token, verify_password

def create_user(db: Session, user: UserCreate):
    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="User email already exists")
    # password_hashed = hash_password(user.password)

    new_user = User(
        name= user.name,
        email= user.email,
        password= user.password,
        user_type= user.user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    # if not user or not verify_password(password, user.password):
    if not user or not password == user.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_access_token(user.id, user.user_type)
    return token

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()
