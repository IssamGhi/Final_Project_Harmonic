from utils.database import db
from sqlalchemy import Table
from models.asso import association


class Issue(db.Model):
    __tablename__ = 'metelyk_issue'

    id_issue = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(50))
    signature = db.Column(db.String(200))
    users = db.relationship('User', secondary= association, back_populates='issues')

    def __init__(self, name, desc, signature, filepath):
        self.name = name
        self.desc = desc
        self.signature = signature
        self.filepath =filepath

    def __str__(self):
        return f"Name: {self.name} desc : {self.desc}: signature : {self.signature} filename : {self.filepath}"

    def __repr__(self):
        return self.__str__()

    def json(self):
        return {'name': self.name, 'desc': self.desc, 'signature': self.signature, 'filepath': self.filepath}

