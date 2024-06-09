from faker import Faker
import json
import time

fake = Faker('en_US')

while True:
    fake_user = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "credential": {
            "username": fake.user_name(),
            "password": fake.password(),
        }, 
        "phone_number": fake.phone_number(),
        "company": fake.company(),
        "job": fake.job(),
        "birthdate": fake.date_of_birth().isoformat(),
    }

    # Convert the dictionary to a JSON string
    fake_user_json = json.dumps(fake_user, indent=4)
    print(fake_user_json)

    time.sleep(1)
