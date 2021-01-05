from psycopg2.extras import RealDictCursor
from iter_file import IteratorFile
from util import get_random_date

import database_common
from random import randint


@database_common.connection_handler
def init_database(cursor: RealDictCursor):
    cursor.execute(open("init.sql", "r").read())


@database_common.connection_handler
def add_cities(cursor: RealDictCursor, cities):
    f = IteratorFile(("{}".format(x) for x in cities))
    cursor.copy_from(f, 'city', columns=(['name']))


@database_common.connection_handler
def add_countries(cursor: RealDictCursor, countries):
    f = IteratorFile(("{}".format(x) for x in countries))
    cursor.copy_from(f, 'country', columns=(['name']))


@database_common.connection_handler
def add_genres(cursor: RealDictCursor, genres):
    f = IteratorFile(("{}".format(x) for x in genres))
    cursor.copy_from(f, 'genre', columns=(['type']))


@database_common.connection_handler
def add_streets(cursor: RealDictCursor, streets):
    f = IteratorFile(("{}".format(x) for x in streets))
    cursor.copy_from(f, 'street', columns=(['name']))


@database_common.connection_handler
def add_studios(cursor: RealDictCursor, studios_data):
    f = IteratorFile(("{}\t{}".format(*studio) for studio in studios_data))
    cursor.copy_from(f, 'studio', columns=(['name', 'address_id']))


@database_common.connection_handler
def add_addresses(cursor: RealDictCursor, addresses_amount: int, countries_amount: int, cities_amount: int,
                  street_amount: int):
    max_local_number = 1000

    f = IteratorFile(("{}\t{}\t{}\t{}".format(randint(1, street_amount),
                                              randint(1, max_local_number),
                                              randint(1, cities_amount),
                                              randint(1, countries_amount)) for _ in range(addresses_amount)))

    cursor.copy_from(f, 'address', columns=(['street_id', 'local_number', 'city_id', 'country_id']))


@database_common.connection_handler
def add_users(cursor: RealDictCursor, users_data):
    f = IteratorFile(("{}\t{}\t{}\t{}".format(*user) for user in users_data))

    cursor.copy_from(f, 'user_account', columns=(['first_name', 'last_name', 'email', 'address_id']))


@database_common.connection_handler
def add_bands(cursor: RealDictCursor, bands_amount: int, bands):
    f = IteratorFile(("{}\t{}".format(bands[randint(1, len(bands) - 1)],
                                      get_random_date()) for _ in range(bands_amount)))

    cursor.copy_from(f, 'band', columns=(['name', 'band_establishment']))
