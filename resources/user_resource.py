from flask_restful import Resource, reqparse, marshal_with
from flask_injector import inject
from flask import jsonify


from services.user_service import UserService
from utils.genric_encoder import GenericEncoder


class UserResource(Resource):

    @inject
    def __init__(self, service: UserService):
        self.user_service = service

    # Creating parser to parse data from rest request
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Add a new user name")
    parser.add_argument("surname", type=str, required=True, help="Add a new user surname")
    parser.add_argument("email", type=str, required=True, help="Add a new user email")
    parser.add_argument("password", type=str, required=True, help="Add a new user password")

    # Save_user
    def post(self):

        data = UserResource.parser.parse_args()
        res = self.user_service.save_user(data["name"], data["surname"], data["email"], data["password"])
        return res.json()




