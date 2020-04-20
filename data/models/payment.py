import datetime
import sqlalchemy
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase
from sqlalchemy import ForeignKey

class Payment(SqlAlchemyBase):
    __tablename__ = 'payment'

    payment_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    payment_type = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    order_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('orders.order_id'))
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(), index=True)
    orders = orm.relation("Orders", back_populates='payment')


