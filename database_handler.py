from psycopg2.extras import RealDictCursor
from iter_file import IteratorFile

import database_common


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
