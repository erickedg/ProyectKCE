from pydantic import BaseModel, Field

class Users(BaseModel):
    iduser: int = 0
    name: str = Field(min_length=1, max_length=25)
    username: str = Field(min_length=1, max_length=20)
    status: bool = True
    
