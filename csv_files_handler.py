import csv


def read_csv_file(name: str):
    data = []
    name_index = 1
    with open("sample_data/" + name + ".csv", "r") as csvfile:
        reader = list(csv.reader(csvfile))

        for line in reader:
            data.append(line[name_index])

    return data
