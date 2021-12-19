import random
import string


from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create fake users'  # noqa: A003

    def randompassword(self):
        chars = string.digits + string.ascii_letters
        return ''.join(random.choice(chars) for _ in range(20))

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11))

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        for i in range(total):
            User.objects.create_user(username=fake.name(),
                                     email=fake.email(),
                                     password=self.randompassword())
