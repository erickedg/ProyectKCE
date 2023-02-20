from fastapi import FastAPI

#importar el archivo de base de datos
from config.database import engine, Base
from routers.product import product_router

app = FastAPI()
app.title = "API del proyecto ProyectKCE"
app.version = "0.0.1"

app.include_router(product_router)

Base.metadata.create_all(bind=engine)
