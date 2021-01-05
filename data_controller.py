from database_handler import *
from csv_files_handler import *
from random import randint
from util import get_random_date, get_random_song_length

FIRST_NAMES = read_csv_file("first_name")
LAST_NAMES = read_csv_file("last_name")

CITIES_AMOUNT = 0
COUNTRIES_AMOUNT = 0
GENRES_AMOUNT = 0
STREETS_AMOUNT = 0
STUDIOS_AMOUNT = 0
ADDRESSES_AMOUNT = 100000
BANDS_AMOUNT = 15000
USERS_AMOUNT = 100000
ARTISTS_AMOUNT = 100000
<<<<<<< HEAD
PLAYLISTS_AMOUNT = 50000
=======
ALBUMS_AMOUNT = 45000
SONGS_AMOUNT = 675000
>>>>>>> master
FIRST_NAMES_AMOUNT = len(FIRST_NAMES)
LAST_NAMES_AMOUNT = len(LAST_NAMES)


def generate_sample_data():
    init_database()
    __generate_addresses()
    __generate_users()
    __generate_bands()
    __generate_studios()
    __generate_albums()
    __generate_artists()
<<<<<<< HEAD
    __generate_playlists()
=======
    __generate_songs()
>>>>>>> master


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


def __generate_artists():
    artist_data = __generate_artists_data()
    add_artists(artist_data)


def __generate_artists_data():
    artists_data = []

    genders = ['male', 'female']
    instruments = read_csv_file("instruments")
    instruments_amount = len(instruments)
    genders_length = len(genders)

    for _ in range(ARTISTS_AMOUNT):
        first_name = FIRST_NAMES[randint(0, FIRST_NAMES_AMOUNT - 1)]
        last_name = LAST_NAMES[randint(0, LAST_NAMES_AMOUNT - 1)]
        gender = genders[randint(0, genders_length - 1)]
        instrument = instruments[randint(0, instruments_amount - 1)]
        artist_data = first_name, last_name, gender, instrument
        artists_data.append(artist_data)

    return artists_data


<<<<<<< HEAD
def __generate_playlists():
    playlists = read_csv_file("playlist")
    add_playlists(PLAYLISTS_AMOUNT, playlists)
=======
def __generate_albums():
    albums_data = __generate_albums_data()
    add_albums(albums_data)


def __generate_albums_data():
    albums_names = read_csv_file('album')
    albums_names_amount = len(albums_names)

    albums_data = []
    for _ in range(ALBUMS_AMOUNT):
        album_name = albums_names[randint(0, albums_names_amount - 1)]
        date = get_random_date()
        studio_id = randint(1, STUDIOS_AMOUNT)
        band_id = randint(1, BANDS_AMOUNT)
        album_data = album_name, date, studio_id, band_id
        albums_data.append(album_data)

    return albums_data


def __generate_songs():
    songs_data = __generate_songs_data()
    add_songs(songs_data)


def __generate_songs_data():
    songs_titles = read_csv_file('songs')
    songs_title_amount = len(songs_titles)

    songs_data = []
    for _ in range(SONGS_AMOUNT):
        song_title = songs_titles[randint(0, songs_title_amount - 1)]
        length = get_random_song_length()
        views = randint(0, 1000000)
        album_id = randint(1, ALBUMS_AMOUNT)
        genre_id = randint(1, GENRES_AMOUNT)

        song_data = song_title, length, views, album_id, genre_id
        songs_data.append(song_data)

    return songs_data
>>>>>>> master
