from models.issue import Issue
from repositories.genric_repository import GenericRepository
from utils.database import db


class IssueRepository(GenericRepository):

        def get_all_issues(self):
            return db.session.query(Issue).all()