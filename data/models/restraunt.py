import datetime
import sqlalchemy
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase

from sqlalchemy import ForeignKey

class Restraunt(SqlAlchemyBase):
    __tablename__ = 'restraunt'

    rest_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    address = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    rating = sqlalchemy.Column(sqlalchemy.Float)
    location = sqlalchemy.Column(sqlalchemy.String)
    menu = orm.relation("Menu", back_populates='restraunt')

