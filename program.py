import datetime
import sys
import ingest_db
from data import sessionfactory
from services import data_service
from infrastructure.numbers import try_int
from infrastructure.switchlang import switch
from time import sleep
user = None

def main():

    setup_db()
    list_restraunts()


    order_rating_fun()

    # options = 'Enter a command, [o]rder, [a]vailable, [l]ocate, [h]istory, e[X]it: '
    # cmd = "NOT SET"

    # while cmd:
    #     cmd = input(options).lower().strip()
    #     with switch(cmd) as s:
    #         #s.case('o', order_food)
    #         s.case('a', list_restraunts)
    #         #s.case('l', list_menu)
    #         #s.case('h', my_history)
    #         #s.case(['x', ''], exit_app)
    #         #s.default(lambda: print(f"Don't know what to do with {cmd}."))
    #

def setup_db():
    global user
    #sessionfactory.global_init('restrauntapp.sqlite')
    sessionfactory.global_init('orders')
    sessionfactory.create_tables()

    # uncomment it later - debugging going
    ingest_db.import_if_empty()
    user = data_service.get_default_user()


def list_restraunts(location='kolkata'):
    user = data_service.get_default_user()
    #print(user)
    restraunt_near = data_service.find_restraunts_near_me(location)
    for rest in restraunt_near:
        print(rest.name)

    #return restraunt_near
    # to be done

def order_rating_fun():
    while True:
        sleep(60)
        data_service.book_order()


#def book_order():


    # to be done

# def order_history():
#
#
#     # to be done
#
# def orders_in_process():
#
#
#     # to be done


if __name__ == '__main__':
    main()
