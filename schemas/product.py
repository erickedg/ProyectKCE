from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=5, max_length=100)
    price: float = Field(ge=1, le=1000000)
    
    
    class Config:
        schema_extra = {
            "example": {
                "id" : 1,
                "name" : "Producto 1",
                "price": 100.88,
            }
        }