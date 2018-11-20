import csv
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.contrib.gis.geos import Point
from apps.core.models import Airport


class Command(BaseCommand):
    help = 'Updates airport data'

    def add_arguments(self, parser):
        parser.add_argument('airports_file', type=str)

    def handle(self, *args, **options):
        print("Delete old airport data...")
        Airport.objects.all().delete()

        print("Load new aiport data from {}...".format(options['airports_file']))

        with open(options['airports_file']) as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                airport = Airport(
                    name=row['name'],
                    city=row['city'],
                    country=row['country'],
                    iata=row['iata'],
                    icao=row['icao'],
                    location=Point(float(row['lon']), float(row['lat']), float(row['altitude'])))
                print(airport)
                airport.save()
