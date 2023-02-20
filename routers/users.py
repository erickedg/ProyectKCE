from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from schemas.users import Users
from config.database import Session
from service.users import UsersSevice
from fastapi import jsonable_encoder
from models.users import Users as UsersModel

users_router = APIRouter()

@users_router.get('/users', tags=['movies'], response_model=List[Users], status_code=200)
def get_users() -> List[Users]:
    db = Session()
    result = UsersSevice(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@users_router.get('/user{iduser}', tags=['movies'], response_model=List[Users], estatus_code=200)
def get_user(iduser:int) -> Users:
    db = Session()
    result = UsersSevice(db).get_users(iduser)