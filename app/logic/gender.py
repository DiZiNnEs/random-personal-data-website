import random

male = 'male'
female = 'female'


def random_gender():
    random_number = random.randrange(2)
    if random_number == 0:
        return male
    else:
        return female
