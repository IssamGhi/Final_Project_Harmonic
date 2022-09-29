from flask_restful import fields
from models.user import User
from models.issue import Issue
user1 = User
resource_user_issue_fields = {
    "user_id": fields.Integer,
    "issue_id": fields.String,
}