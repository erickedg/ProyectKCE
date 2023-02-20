from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Users(Base):
    __tablename__="users"
    
    iduser = Column(Integer, primary_key = True)
    name = Column(String)
    username = Column(String)
    status = Column(Boolean)