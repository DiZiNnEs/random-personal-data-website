import random
import string

rnd_number = lambda: random.randrange(10, 35)


def randomString():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(rnd_number()))
