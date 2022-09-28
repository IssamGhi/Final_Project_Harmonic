from flask_injector import inject
from flask_jwt_extended import create_access_token
from models.user import User
from repositories.user_repository import UserRepository
from utils.genric_encoder import GenericEncoder


class UserService:
    @inject
    def __init__(self, repository: UserRepository):
        self.repository = repository

    # Enregisteration of the user
    def save_user(self, name, surname, email, password):
        user = User(name,surname, email, password, False)
        return self.repository.save(user)

        #Login service of the user or admin
    def login_user(self, email, password):
        user = self.repository.find_user_by_email(email)
        #Login of developer
        if user is not None and not user.role:
            ##Check hash password
            if user.password == password:
                ###Create token
                token = create_access_token(user.email, additional_claims={'role': False})
                return token
        elif user is not None and user.role:
            #Admin login
            if user.password == password:
                ###Create token
                token = create_access_token(user.email, additional_claims={'role': True})
                return token
        else:
            return {"message": "wrong user or password"}, 401



