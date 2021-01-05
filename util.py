import random
import datetime


# create function accepting a single parameter, the year as a four digit number
def get_random_date():
    year = random.randint(1945, 2000)
    # try to get a date
    try:
        return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')

    # if the value happens to be in the leap year range, try again
    except ValueError:
        return get_random_date(year)


def get_random_song_length():
    return f'{random.randint(1, 10)}min {random.randint(0, 59)}sec'
