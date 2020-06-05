import random
import string

from .first_name import first_name_function as fnf
from .last_name import last_name_function as lnf

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
email = ['@gmail.com', '@mail.ru', '@yandex.ru', '@yahoo.com']

rnd_lowercase = lambda: lowercase[random.randrange(26)]
rnd_uppercase = lambda: uppercase[random.randrange(26)]
rnd_digits = lambda: digits[random.randrange(10)]
rnd_email = lambda: email[random.randrange(3)]


def send_email():
    return fnf() + lnf() + rnd_lowercase() + rnd_uppercase() + rnd_digits() + rnd_digits() + rnd_email()
