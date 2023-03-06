from models.users import Users as UsersModel
from schemas.users import Users

class UsersSevice():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_users(self):
        result = self.db.query(UsersModel).all()
        return result

    def get_user(self, id:int):
        result = self.db.query(UsersModel).filter(UsersModel.iduser == id).first()
        return result

    def create_user(self, users:Users):
        new_user = UsersModel(**users.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def update_user(self, id:int, data:Users):
        user = self.db.query(UsersModel).filter(UsersModel.iduser == id).first()
        user.name = data.name
        user.username = data.username
        user.status = data.status
        self.db.commit()
        return

    def delete_user(self, id:int):
        self.db.query(UsersModel).filter(UsersModel.iduser == id).delete()
        self.db.commit()
        return