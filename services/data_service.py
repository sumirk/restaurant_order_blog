import datetime
import random
from typing import List

from data import sessionfactory
from data.models.customer import Customer
from data.models.menu import Menu
from data.models.orders import Orders
from data.models.payment import Payment
from data.models.restraunt import Restraunt


def get_default_user():
    session = sessionfactory.create_session()

    customer = session.query(Customer).filter(Customer.email == 'test@gmail.com').all()

    if customer:
        return customer

    customer = Customer()
    customer.name = 'test_user'
    customer.email = 'test@gmail.com'
    customer.address = 'Bangalore'
    customer.phone = '9876543210'
    session.add(customer)

    session.commit()
    customer1 = Customer()
    customer1.name = 'test_user1'
    customer1.email = 'test1@gmail.com'
    customer1.address = 'Bangalore'
    customer1.phone = '9876543211'
    session.add(customer1)

    session.commit()

    customer2 = Customer()
    customer2.name = 'test_user2'
    customer2.email = 'test3@gmail.com'
    customer2.address = 'kolkata'
    customer2.phone = '9876543212'
    session.add(customer2)

    session.commit()
def find_restraunts_near_me(loc):
    session = sessionfactory.create_session()
    near_restraunts = session.query(Restraunt).filter(Restraunt.location==loc).all()
    #breakpoint()
    return near_restraunts

def list_menu_restraunt(rest_id):
    session = sessionfactory.create_session()

    menu_list = session.query(Menu).filter(Menu.restraunt_id == rest_id).all()
    return menu_list

def book_order():
    session = sessionfactory.create_session()
    restraunt = session.query(Restraunt.rest_id).all()
    restraunt_select = random.choice(restraunt)[0]
    # validate below to check if customer is valid
    customer_id = session.query(Customer.cust_id).filter(Customer.email == random.choice(['test@gmail.com', 'test1@gmail.com', 'test2@gmail.com'])).all()[0][0]

    try:
        menu_id = session.query(Menu.menu_id).filter(Menu.restraunt_id == restraunt_select).first()[0]
    except:
        menu_id = None

    new_order = Orders()
    new_order.customer_id = customer_id
    new_order.restraunt_id = restraunt_select
    new_order.menu_id = menu_id
    new_order.feedback = random.randint(1,5)
    new_order.total_price = random.randint(200,400)
    new_order.created_at = datetime.datetime.now()

    session.add(new_order)
    #breakpoint()
    session.commit()
    rating(restraunt_select)


def rating(restraunt_id):
    session = sessionfactory.create_session()
    rest = session.query(Restraunt).get(restraunt_id)
    rest.rating = round(random.uniform(3.0,4.9), 2)
    session.add(rest)
    session.commit()
