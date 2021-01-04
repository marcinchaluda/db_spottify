import csv


def read_cities_from_files():
    cities = []
    with open("sample_data/cities.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            cities.append(line[1])

    return cities
