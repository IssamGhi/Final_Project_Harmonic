from flask_restful import fields

resource_issues_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "desc": fields.String,
    "signature": fields.String

}
