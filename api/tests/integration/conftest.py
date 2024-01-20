import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import delete, insert

from db.engine import engine
from db.user import User


@pytest.fixture(scope="session")
def api_client():
    return TestClient(app)


def clean_db():
    with engine.begin() as connection:
        connection.execute(delete(User))


@pytest.fixture(autouse=True)
def post_clean_db():
    yield
    clean_db()


def insert_user_with_id(user_id: int, name: str, email: str):
    with engine.begin() as connection:
        connection.execute(
            insert(User).values(id=user_id, name=name, email=email)
        )


@pytest.fixture
def set_up_users(users):
    for index, user in enumerate(users):
        insert_user_with_id(user_id=index + 1, **user)
