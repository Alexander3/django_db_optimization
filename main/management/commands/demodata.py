import random
import sys

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command
from main.models import Customer, Manager
from mixer.backend.django import Mixer

User = get_user_model()
mixer = Mixer()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_user()
        manager = None
        for i in range(400000):
            if i == 0 or i % 3:
                manager = mixer.blend(Manager)

            mixer.blend(
                Customer,
                phone_number=random.choice([mixer.faker.phone_number(), None]),
                manager=manager,
            )
            if i % 10000 == 0:
                self.stdout.write(f"Added {i} customers")

    def create_user(self):
        credentials = {
            "username": "demo@demo.com",
            "email": "demo@demo.com",
            "password": "demo123",
        }
        if User.objects.filter(username=credentials["email"]).exists():
            confirmation = input(
                "demo Superuser already exists, do you want to flush db? [Y/n]"
            ).lower()
            if confirmation == "" or confirmation == "y":
                call_command("flush", interactive=False)
            else:
                sys.exit(1)

        User.objects.create_superuser(**credentials)
        self.stdout.write(
            "Created admin user with following credentials:\nUsername: {username}\nPassword: {password}".format(
                **credentials
            )
        )
