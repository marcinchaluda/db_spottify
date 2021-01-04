from database_handler import *
from csv_files_handler import read_cities_from_files

CITIES_AMOUNT = 0


def generate_sample_data():
    init_database()
    __insert_cities()


def __insert_cities():
    global CITIES_AMOUNT
    cities = read_cities_from_files()
    add_city(cities)
    CITIES_AMOUNT = len(cities)
