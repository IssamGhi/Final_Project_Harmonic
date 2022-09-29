from utils.database import db
from sqlalchemy import Table, Column, Integer, String, ForeignKey


association = db.Table(
    'user_issue',
    db.Column('user_id', ForeignKey("metelyk_user.id_user", ondelete='CASCADE', onupdate='CASCADE')),
    db.Column('issue_id', ForeignKey('metelyk_issue.id_issue', onupdate='CASCADE', ondelete='CASCADE')),
    db.Column('result_id', Integer)
)