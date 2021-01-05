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


def get_first_names():
    first_names = []

    first_name_index = 1
    with open("sample_data/first_name.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            first_names.append(line[first_name_index])

    return first_names


def get_last_names():
    last_names = []

    last_name_index = 1
    with open("sample_data/last_name.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            last_names.append(line[last_name_index])

    return last_names


def get_domains():
    domains = []

    domain_index = 1
    with open("sample_data/domain.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            domains.append(line[domain_index])

    return domains


def read_bands_from_file():
    bands = []
    band_name = 1
    with open("sample_data/band_name.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            bands.append(line[band_name])

    return bands
