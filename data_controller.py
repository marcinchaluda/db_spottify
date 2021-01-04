from database_handler import *
from csv_files_handler import *

CITIES_AMOUNT = 0
COUNTRIES_AMOUNT = 0


def generate_sample_data():
    init_database()
    __insert_cities()
    __insert_countries()


def __insert_cities():
    global CITIES_AMOUNT
    cities = read_cities_from_files()
    add_cities(cities)
    CITIES_AMOUNT = len(cities)


def __insert_countries():
    global COUNTRIES_AMOUNT
    countries = read_countries_from_files()
    add_countries(countries)
    COUNTRIES_AMOUNT = len(countries)
