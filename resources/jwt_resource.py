from flask import request
from flask_jwt_extended import jwt_required, get_jwt
from flask_restful import Resource
from injector import inject
import postgres

from services.identification_service import IdentificationService


class JwtResource(Resource):

    @inject
    def __init__(self, service:IdentificationService):
        self.service = service

    @jwt_required()
    def post(self):
        # FROM metelyk_user SELECT id_user WHERE role = True
        pass


    @jwt_required()
    def get(self):
        pass