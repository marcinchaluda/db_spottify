from psycopg2.extras import RealDictCursor
from iter_file import IteratorFile

import database_common


@database_common.connection_handler
def init_database(cursor: RealDictCursor):
    cursor.execute(open("init.sql", "r").read())


@database_common.connection_handler
def add_city(cursor: RealDictCursor, cities):
    f = IteratorFile(("{}".format(x) for x in cities))
    cursor.copy_from(f, 'city', columns=(['name']))
