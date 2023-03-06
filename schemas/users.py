from pydantic import BaseModel, Field
from typing import Optional

class Users(BaseModel):
    iduser: Optional[int] = None
    name: str = Field(min_length=1, max_length=25)
    username: str = Field(min_length=1, max_length=20)
    status: bool = True
    
    class Config:
        schema_extra = {
            "example": {
                "iduser": 1,
                "name": "Nombre",
                "username": "Usuario",
                "status": True
            }
        }