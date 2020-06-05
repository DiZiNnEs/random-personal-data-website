from faker import Faker

fake = Faker()

fake_address = lambda: fake.address()
print(fake_address())
