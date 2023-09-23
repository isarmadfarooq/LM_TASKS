from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import datetime
import pytz
from enroll.models import TimeTrackinEntry


class Command(BaseCommand):
    help = "Insert Dummy users and PST date times into the database"

    def handle(self, *args, **options):
        self.insert_dummy_users()

        self.insert_pst_date_times()

        self.stdout.write(self.style.SUCCESS("Successfully inserted dummy data"))

    def insert_dummy_users(self):
        for i in range(1, 11):
            username = f"user{i}"
            email = f"user{i}@exmple.com"
            password = "password123"
            user, created = User.objects.get_or_create(
                username=username, email=email, password=password
            )
            if not created:
                user.save()
            self.stdout.write(self.style.SUCCESS(f"create a {username}"))

    def insert_pst_date_times(self):
        pst = pytz.timezone("US/Pacific")
        current_time = datetime.now(pst)

        for _ in range(100):
            time = TimeTrackinEntry.objects.create(datetime_col=current_time)
            time.save()
            self.stdout.write(self.style.SUCCESS("create a PSTDateTime entry"), time)
