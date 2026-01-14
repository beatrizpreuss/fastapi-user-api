# FastAPI app

from fastapi import FastAPI, Depends, HTTPException
from .models import User
from .schemas import UserCreate, UserResponse, UserUpdate
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


@app.get("/users/{user_id}", response_model=UserResponse) #define path parameter using user id, and make whatever is returned match UserResponse
def get_user(user_id: int, db: Session = Depends(get_db)): #define function that will run when endpoint is called. db Session is a dependency injection that calls get_db and injects its return value here (db becomes a SQLAlchemy Session).
    db_user = db.get(User, user_id) #query the database (fetches 1 row by primary key). User is the model class that maps to a database table.

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id) #fetch existing user

    if not db_user: #check existence
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name #update fields

    db.commit() #commit and refresh
    db.refresh(db_user)

    return db_user