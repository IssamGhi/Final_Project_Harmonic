from flask_restful import Resource, reqparse, marshal_with
from flask_injector import inject
from flask import request
from flask import jsonify

from services.issue_service import IssueService
from utils.genric_encoder import GenericEncoder


class IssueResource(Resource):

    @inject
    def init(self, service: IssueService):
        self.issue_service = service

    # Creating parser to parse data from rest request
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Add a name for the issue")
    parser.add_argument("desc", type=str, required=True, help="Add a description for the issue")
    parser.add_argument("signature", type=str, required=True, help="Add signature")

    # Save_issue
    def post(self):
        filepath = self.issue_service.upload_file(request.files['filename'])
        data = IssueResource.parser.parse_args()
        return self.issue_service.save_issue(data["name"], data["desc"], data["signature"], filepath).json()

    def get(self):
        return self.issue_service.get_all_issues().json()