from flask_injector import inject
from flask_jwt_extended import create_access_token
from flask_restful import marshal_with

from models.user import User
from models.asso import association
from repositories.user_repository import UserRepository
from repositories.user_issue import UserIssueRepository
from utils.genric_encoder import GenericEncoder
from models.issue import Issue
from models.asso import association
import jsonify
from fields.user_issue_dto import resource_user_issue_fields


import os
class UserIssueService:
    @inject
    def __init__(self, repository: UserIssueRepository):
        self.repository = repository

    # def save_user_issue(self, user_id, issue_id):
    #     relation = (user_id, issue_id)
    #     return self.repository.save(relation)


    @marshal_with(resource_user_issue_fields)
    def get_all_user_issue(self):
        return self.repository.add_ex_to_user()