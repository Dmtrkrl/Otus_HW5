import random
import string
from random import randint


def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_phone():
    return "".join([random.choice(string.digits) for _ in range(10)])


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])


def random_login():
    return random_string() + str(randint(1, 999))


def random_price():
    return str(randint(1000, 5000))
