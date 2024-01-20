import logging

import schemas.user as user_schemas
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db.engine import SessionLocal
from db.user import create_user, get_user, get_user_by_email, get_users

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.post("/users/", response_model=user_schemas.User)
def post_create_user(
    user: user_schemas.UserCreate, db: Session = Depends(get_db)
):
    logging.info("Receieved create_user request")
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@app.get("/users/", response_model=list[user_schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users


@app.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
