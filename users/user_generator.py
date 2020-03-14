from faker import Faker
from users.user import User
import json


class UserGenerator():
    @staticmethod
    def generate_random_user():
        fake = Faker()
        profile = fake.simple_profile()
        last_name = profile["name"].split(' ')[1]
        return User(username=profile["username"] + last_name, email=last_name + profile["mail"], password=fake.password())

    @staticmethod
    def generate_from_json(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
        return User(username=data['username'], email=data['email'], password=data['password'])
