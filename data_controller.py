from database_handler import *
from csv_files_handler import *

CITIES_AMOUNT = 0
COUNTRIES_AMOUNT = 0
GENRES_AMOUNT = 0
STREETS_AMOUNT = 0


def generate_sample_data():
    init_database()
    __insert_cities()
    __insert_countries()
    __insert_genres()
    __insert_streets()


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


def __insert_genres():
    global GENRES_AMOUNT
    genres = read_genres_from_file()
    add_genres(genres)
    GENRES_AMOUNT = len(genres)


def __insert_streets():
    global STREETS_AMOUNT
    streets = read_street_names_from_files()
    add_streets(streets)
    STREETS_AMOUNT = len(streets)
