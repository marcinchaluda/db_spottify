from database_handler import *
from csv_files_handler import *
from random import randint

FIRST_NAMES = read_csv_file("first_name")
LAST_NAMES = read_csv_file("last_name")

CITIES_AMOUNT = 0
COUNTRIES_AMOUNT = 0
GENRES_AMOUNT = 0
STREETS_AMOUNT = 0
STUDIOS_AMOUNT = 0
ADDRESSES_AMOUNT = 10000
BANDS_AMOUNT = 15000
USERS_AMOUNT = 10000
FIRST_NAMES_AMOUNT = len(FIRST_NAMES)
LAST_NAMES_AMOUNT = len(LAST_NAMES)


def generate_sample_data():
    init_database()
    __generate_addresses()
    __generate_users()
    __generate_bands()
    __generate_studios()


def __generate_addresses():
    __insert_cities()
    __insert_countries()
    __insert_genres()
    __insert_streets()
    add_addresses(ADDRESSES_AMOUNT, COUNTRIES_AMOUNT, CITIES_AMOUNT, STREETS_AMOUNT)


def __generate_bands():
    bands = read_csv_file("band_name")
    add_bands(BANDS_AMOUNT, bands)


def __insert_cities():
    global CITIES_AMOUNT
    cities = read_csv_file("cities")
    add_cities(cities)
    CITIES_AMOUNT = len(cities)


def __insert_countries():
    global COUNTRIES_AMOUNT
    countries = read_csv_file("country")
    add_countries(countries)
    COUNTRIES_AMOUNT = len(countries)


def __insert_genres():
    global GENRES_AMOUNT
    genres = read_csv_file("genres")
    add_genres(genres)
    GENRES_AMOUNT = len(genres)


def __insert_streets():
    global STREETS_AMOUNT
    streets = read_csv_file("street_name")
    add_streets(streets)
    STREETS_AMOUNT = len(streets)


def __generate_users():
    users_data = __generate_users_data()
    add_users(users_data)


def __generate_users_data():
    users_data = []

    domains = read_csv_file("domain")
    domains_amount = len(domains)

    for _ in range(USERS_AMOUNT):
        first_name = FIRST_NAMES[randint(0, FIRST_NAMES_AMOUNT - 1)]
        last_name = LAST_NAMES[randint(0, LAST_NAMES_AMOUNT - 1)]
        email = first_name[:3] + last_name[:3] + '@' + domains[randint(0, domains_amount - 1)]
        user_data = first_name, last_name, email, randint(1, ADDRESSES_AMOUNT)
        users_data.append(user_data)

    return users_data


def __generate_studios():
    global STUDIOS_AMOUNT
    studios = read_csv_file("street_name")
    STUDIOS_AMOUNT = len(studios)

    studios_data = []
    for studio in studios:
        studios_data.append((studio, randint(1, ADDRESSES_AMOUNT)))

    add_studios(studios_data)

