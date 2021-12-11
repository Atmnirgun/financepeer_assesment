from db.orm import db
from models.user_dto import UserDTO
from db.entities import User

class UserService():

    def get_user_by_username(self,username:str):
        user = User.query.filter_by(user_name=username).first()
        return user

    






