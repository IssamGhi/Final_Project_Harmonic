from flask_restful import fields

resource_issues_fields = {
    "name": fields.String,
    "desc": fields.String,
    "signature": fields.String

}
