from faker import Faker

fake = Faker()

fake_bio = lambda: fake.text()
