from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.user_service import UserService
from ..schemas import schemas_user
from ..services import user_service
from ..models.user_models import get_db

router = APIRouter()
user_service_test = UserService()

@router.get("/users")
async def get_users():
    return await user_service_test.get_users()


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return await user_service_test.get_user_by_id(user_id)

@router.post("/create-users/")
def create_user(user: schemas_user.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db=db, user=user)

@router.get("/get-all-users")
async def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_users(db = db)