from typing import List

from app.models.user_models import User
from sqlalchemy.orm import Session
from ..services import *
from ..models import user_models
from ..schemas import schemas_user


def create_user(db: Session, user: schemas_user.UserCreate):
    db_user = user_models.User(username=user.username, email=user.email)
    db_user.password = user.password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(user_models.User).all()

class UserService:
    async def get_users(self) -> List[User]:
        # Lấy danh sách user từ database
        # ...
        return [User(id=1, username="user1", email="user1@example.com")]

    async def get_user_by_id(self, user_id: int) -> User:
        # Lấy user từ database bằng id
        # ...
        return User(id=user_id, username="user1", email="user1@example.com")
