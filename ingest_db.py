from random import randint
import random
from services import data_service
from data import sessionfactory
from data.models.customer import Customer
from data.models.restraunt import Restraunt
from data.models.menu import Menu



def import_if_empty():
    __import_customer()
    __import_restraunt()
    __import_menu()


def __import_customer():
    session = sessionfactory.create_session()
    #breakpoint()in
    if session.query(Customer).count() > 0:
        return

    data_service.get_default_user()

    customer2 = Customer()
    customer2.name = 'test_user_2'
    customer2.address = 'Bangalore'
    customer2.email = 'test2@gmail.com'
    customer2.phone = '9876123451'
    session.add(customer2)
    session.commit()

def __import_restraunt():

    restraunt_name = 'pizza_hut papa_johns star_bucks mc_donalds red_dragon blue_frog '.split()
    session = sessionfactory.create_session()
    if session.query(Restraunt).count() > 0:
        return

    location = 'bangalore delhi mumbai kolkata chennai hyderabad jaipur'.split()
    n = 10

    Count = 11
    for _ in range(0, 200):

            #rest in restraunt_name:
            restraunt = Restraunt()
            restraunt.name = 'restaurant' + str(random.randint(1,1000))
            restraunt.phone = ''.join([f'{randint(0,9)}' for num in range(0,n)])

            restraunt.location = random.choice(location)
            session.add(restraunt)
            session.commit()



def __import_menu():
    session = sessionfactory.create_session()
    if session.query(Menu).count() > 0:
        return
    #restraunt_name = 'pizza_hut papa_johns star_bucks mc_donalds red_dragon blue_frog al_kareem'.split()
    menu_items = 'chinese indian continental korean japanese mediterranean'.split()

    restraunt = (session.query(Restraunt).all())


    Count = 11
    for _ in range(0, 11):
    #for rest in restraunt:

        menu = Menu()
        menu.restraunt_id = (random.choice(restraunt)).rest_id
        menu.price = random.randint(100,300)
        menu.menu_name = random.choice(menu_items)
        menu.menu_ttd = random.randint(20,45)
        session.add(menu)
        session.commit()
