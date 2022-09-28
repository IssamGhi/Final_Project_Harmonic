from models.asso import Asso
from repositories.genric_repository import GenericRepository
from utils.database import db


class SolutionRepository(GenericRepository):

    def get_solution_without_result(self):
        # TODO: add method to get filepaths to test and solution
        # asso = db.session.query(Asso).filter_by(result_id=None).one_or_none()
        # issue = db.session.query(Asso).filter_by(issue_id=asso.issue_id).one_or_none()
        pass

