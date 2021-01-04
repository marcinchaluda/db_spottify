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
