from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from schemas.users import Users
from config.database import Session
from service.users import UsersSevice
from fastapi.encoders import jsonable_encoder
from models.users import Users as UsersModel

users_router = APIRouter()

@users_router.get('/users', tags=['Users'], response_model=List[Users], status_code=200)
def get_users() -> List[Users]:
    db = Session()
    result = UsersSevice(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@users_router.get('/users/{iduser}', tags=['Users'], response_model=List[Users], status_code=200)
def get_user(iduser:int) -> Users:
    db = Session()
    result = UsersSevice(db).get_users(iduser)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@users_router.post('/users', tags=['Users'], response_model=dict, status_code=201)
def create_user(user: Users) -> dict:
    db = Session()
    UsersSevice(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario con exito"})

@users_router.put('/users/{iduser}', tags=['Users'], status_code=200)
def update_user(iduser:int) -> dict:
    db = Session()
    result = UsersSevice(db).update_user(iduser)
    return JSONResponse(status_code=201, content={"message": "Se ha a actualizado el usuario"})

@users_router.delete('/users/{iduser}', tags=['Users'], status_code=200)
def delete_user(iduser:int) -> dict:
    db = Session()
    result = UsersSevice(db).delete_user(iduser)
    return JSONResponse(status_code=201, content={"message" "Se elimino el usuario"})