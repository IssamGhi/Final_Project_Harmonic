from models.issue import Issue
from models.user import User

from models.asso import association
from repositories.genric_repository import GenericRepository
from utils.database import db
from utils.genric_encoder import GenericEncoder


class UserIssueRepository(GenericRepository):

        def add_ex_to_user(self):
            user1 = db.session.query(User).filter(User.name == 'john').first()
            issue1 = db.session.query(Issue).filter(Issue.name == 'Exercice addition').first()
            issue1.users.append(user1)
            db.session.commit()
            for r in user1.issues:
                print(r.name)
            result = db.session.query(association).all()
            return db.session.query(association).all()