import datetime
import sqlalchemy
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase
from sqlalchemy import ForeignKey

class Orders(SqlAlchemyBase):
    __tablename__ = 'orders'

    order_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    customer_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('customer.cust_id'))
    #timing = sqlalchemy.Column(sqlalchemy.Integer)
    total_price = sqlalchemy.Column(sqlalchemy.String, index=True)

    # later to be added for multiple menu
    menu_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('menu.menu_id'))
    restraunt_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('restraunt.rest_id'))
    feedback = sqlalchemy.Column(sqlalchemy.Integer)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(), index=True)
    #completed_at = sqlalchemy.Column(sqlalchemy.DateTime, index=True)

    #menu_name = sqlalchemy.Column(sqlalchemy.String, ForeignKey(), index=True)
    customer = orm.relation("Customer", back_populates='orders')

    menu = orm.relation("Menu", back_populates='orders')
    payment = orm.relation("Payment", back_populates='orders')
    # Validate below line
    #menu_price = Menu.price



