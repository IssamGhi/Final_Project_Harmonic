from flask_injector import inject
from flask_restful import marshal_with
from repositories.user_issue import UserIssueRepository
from fields.user_issue_dto import resource_user_issue_fields


class UserIssueService:
    @inject
    def __init__(self, repository: UserIssueRepository):
        self.repository = repository


    @marshal_with(resource_user_issue_fields)
    def get_all_user_issue(self):
        return self.repository.add_ex_to_user()

    def save_user_issue(self):
        #TODO: develop this function to save developer's exercise to DB
        pass