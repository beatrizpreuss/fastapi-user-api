# FastAPI app

from fastapi import FastAPI, Depends, HTTPException
from .models import User
from .schemas import UserCreate, UserResponse
from .database import get_db
from sqlalchemy.orm import Session


app = FastAPI(title="User Management API")

@app.get("/health")
def health_check():
    return{ "status": "ok"}

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user