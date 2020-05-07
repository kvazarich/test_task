import os
import random
import argparse

import django
from faker import Faker
from django.core.files.images import ImageFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task.settings')
django.setup()

from human_app.models import Human


def create_human():
    fake = Faker()
    human = Human(
        avatar=ImageFile(open('static/avatar_sample.jpg', 'rb')),
        first_name=fake.first_name(),
        second_name=fake.last_name(),
        age=fake.random_number(),
        gender=random.choice(['M', 'F'])
    )
    human.save()


def populate(count):
    for i in range(count):
        create_human()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', metavar='n', type=int, default=10)
    args = parser.parse_args()
    populate(args.n)
