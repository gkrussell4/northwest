import random
import datetime
from northwest.models import Airport, Flight
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'creates a random list of flights'

    def handle(self, *args, **options):
        flights = []
        for i in range(100):
            origin = random.choice(Airport)
            destination = random.choice(Airport)
        while origin == destination:
            destination = random.choice(Airport)
            departure_time = datetime.datetime.now().replace(hour=random.randint(0, 23), minute=random.randint(0, 59))
            duration = datetime.timedelta(minutes=random.randint(30, 300))
            arrival_time = departure_time + duration
            flight = Flight(
                origin=origin,
                destination=destination,
                departure_time=departure_time,
                arrival_time=arrival_time,
                duration=duration
            )
        flights.append(flight)
        Flight.objects.bulk_create(flights)