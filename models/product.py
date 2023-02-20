from sqlalchemy import Column, Integer, String, Float

class Product():
    __tablename__ = "products"

    id = Column(Integer, primary_key = True)
    name = Column(String),
    price = Column(Float)
