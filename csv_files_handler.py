import csv


def read_cities_from_files():
    cities = []
    city_name = 1
    with open("sample_data/cities.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            cities.append(line[city_name])

    return cities


def read_countries_from_files():
    countries = []
    country_name = 1
    with open("sample_data/country.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            countries.append(line[country_name])

    return countries


def read_genres_from_file():
    genres = []
    genre_name = 1
    with open("sample_data/genres.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            genres.append(line[genre_name])

    return genres


def read_street_names_from_files():
    streets = []
    country_name = 1
    with open("sample_data/street_name.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            streets.append(line[country_name])

    return streets
