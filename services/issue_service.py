from flask_injector import inject
from flask_jwt_extended import create_access_token
from flask_restful import marshal_with

from models.user import User
from repositories.user_repository import UserRepository
from repositories.issue_repository import IssueRepository
from utils.genric_encoder import GenericEncoder
from models.issue import Issue
import jsonify
from fields.issue_fields_dto import resource_issues_fields

import os

METELYK_REPOSITORY_PATH='./issuefolder'
class IssueService:

    @inject
    def __init__(self, repository:IssueRepository):
        self.repository = repository

    def upload_file(self, file):
        # create the folder if it does not exist
        if not os.path.exists(METELYK_REPOSITORY_PATH):
            os.makedirs(METELYK_REPOSITORY_PATH)
        # save the file
        filepath= METELYK_REPOSITORY_PATH+ '/' + file.filename
        file.save(os.path.join(METELYK_REPOSITORY_PATH, file.filename))
        return filepath

    def save_issue(self, name, desc, signature):
        # filepath
        issue = Issue(name, desc, signature)
        return self.repository.save(issue)
    @marshal_with(resource_issues_fields)
    def get_all_issues(self):
        return self.repository.get_all_issues()

