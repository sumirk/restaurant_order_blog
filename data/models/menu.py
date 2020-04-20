import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy import ForeignKey
from data.sqlalchemybase import SqlAlchemyBase
from sqlalchemy import ForeignKey

class Menu(SqlAlchemyBase):
    __tablename__ = 'menu'

    menu_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    menu_name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    menu_ttd = sqlalchemy.Column(sqlalchemy.Integer)
    price = sqlalchemy.Column(sqlalchemy.String)
    restraunt_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('restraunt.rest_id'))

    restraunt = orm.relation("Restraunt", back_populates='menu')

    orders = orm.relation("Orders", back_populates='menu')

