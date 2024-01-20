import logging

from schemas.user import UserCreate
from sqlalchemy.orm import Mapped, Session, mapped_column

from db.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    logging.info("Getting user by email")
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session) -> list[User]:
    return db.query(User).all()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
