from utils.database import db
from sqlalchemy import Table
from models.asso import association
from models.issue import Issue

class User(db.Model):
    __tablename__ = 'metelyk_user'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.Boolean)
    issues = db.relationship('Issue', secondary=association, back_populates='users')

    def __init__(self, name, surname, email, password, role):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.role = role


    def __str__(self, name, surname, email, password):
        return f"Name: {self.name} surname : {self.surname}: email : {self.email}"

    def __repr__(self):
        return self.__str__()

    def json(self):
        return {'name': self.name, 'surname': self.surname, 'email': self.email, 'password': self.password,
                'role': self.role}

