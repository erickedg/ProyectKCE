from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse

from typing import List
from config.database import Session
from models.product import Product
from fastapi.encoders import jsonable_encoder
from service.product import ProductService
from schemas.product import Product

product_router = APIRouter()

@product_router.get('/products', tags=['products'], response_model=List[Product], status_code=200)
def get_product() -> List[Product]:
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.get('/products/{id}', tags=['products'], response_model=Product)
def get_product(id: int) -> Product:
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))
@product_router.get('/products/', tags=['products'], response_model=List[Product])
def get_products_by_name(name: str = Query(min_length=3, max_length=100)) -> List[Product]:
    db = Session()
    result = ProductService(db).get_products_by_name(name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.post('/products', tags=['products'], response_model=dict, status_code=201)
def create_product(product: Product) -> dict:
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(status_code=201, content={'message': 'Se registro el producto'})

@product_router.put('/products/{id}', tags=['products'], response_model=dict, status_code=200)
def update_product(id: int, product: Product) -> dict:
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        JSONResponse(status_code=404, content={'message': 'No encontrado'})

    ProductService(db).update_product(id, product)

    return JSONResponse(status_code=200, content={'message': 'Se ha modificado la pelicula'})

@product_router.delete('/products/{id}', tags=['products'], response_model=dict, status_code=200)
def delete_product(id: int) -> dict:
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    ProductService(db).delete_product(id)
    return JSONResponse(status_code=200, content={'message', 'Se ha eliminado el producto'})