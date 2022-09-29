from flask_restful import Resource, reqparse
from flask_injector import inject

from services.user_issue_service import UserIssueService

class UserIssueResource(Resource):
    @inject
    def __init__(self, service: UserIssueService):
        self.user_issue_service = service

    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=int, required=True, help="user who choose issue")
    parser.add_argument("issue_id", type=int, required=True, help="issue choosen for user")

    def post(self):
        data = UserIssueResource.parser.parse_args()
        res = self.user_issue_service.save_user_issue(data["user_id"], data["issue_id"])
        return res.json()

    def get(self):
        return self.user_issue_service.get_all_user_issue()
