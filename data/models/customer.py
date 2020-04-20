import datetime
import sqlalchemy
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase
from sqlalchemy import ForeignKey

class Customer(SqlAlchemyBase):
    __tablename__ = 'customer'

    cust_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    address = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    orders = orm.relation("Orders", back_populates='customer')
