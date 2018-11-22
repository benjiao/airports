import csv
import os
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.contrib.gis.geos import Point
from apps.core.models import Airport
from apps.core.models import Airline
from apps.core.models import Equipment
from apps.core.models import Route
from tqdm import tqdm


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Command(BaseCommand):
    help = 'Updates airport data'

    def add_arguments(self, parser):
        parser.add_argument('data_dir', type=str)

    def handle(self, *args, **options):

        print("Delete old airport data...")
        Airport.objects.all().delete()
        print("Load new aiport data from {}...".format(os.path.join(options['data_dir'], 'airports.csv')))

        with open(os.path.join(options['data_dir'], 'airports.csv')) as f:
            csv_reader = csv.DictReader(f)
            for row in tqdm(csv_reader):
                airport = Airport(
                    name=row['name'],
                    city=row['city'],
                    country=row['country'],
                    iata=row['iata'] if row['iata'].isalnum() else None,
                    icao=row['icao'] if row['icao'].isalnum() else None,
                    location=Point(float(row['lon']), float(row['lat']), float(row['altitude'])),
                    evcent=row['evcent'] if is_float(row['evcent']) else None,
                    pagerank=row['pagerank'] if is_float(row['pagerank']) else None,
                    degree=row['degree_centrality'] if is_float(row['degree_centrality']) else None)
                airport.save()

        print("Delete old airline data...")
        Airline.objects.all().delete()
        print("Load new airline data from {}...".format(os.path.join(options['data_dir'], 'airlines.csv')))

        with open(os.path.join(options['data_dir'], 'airlines.csv')) as f:
            csv_reader = csv.DictReader(f)
            for row in tqdm(csv_reader):
                airport = Airline(
                    name=row['name'],
                    alias=row['alias'],
                    iata=row['iata'] if row['iata'].isalnum() else None,
                    icao=row['icao'] if row['icao'].isalnum() else None,
                    callsign=row['callsign'],
                    country=row['country'],
                    active=row['active'] == 'Y',
                    openflights_id=row['id'])
                airport.save()

        print("Delete old equipment data...")
        Equipment.objects.all().delete()
        print("Load new equpment data from {}...".format(os.path.join(options['data_dir'], 'planes.csv')))

        with open(os.path.join(options['data_dir'], 'planes.csv')) as f:
            csv_reader = csv.DictReader(f)
            for row in tqdm(csv_reader):
                equpment = Equipment(
                    name=row['name'],
                    iata=row['iata'] if row['iata'].isalnum() else None,
                    icao=row['icao'] if row['icao'].isalnum() else None)
                equpment.save()

        print("Delete old routes data...")
        Route.objects.all().delete()
        print("Load new routes data from {}...".format(os.path.join(options['data_dir'], 'routes.csv')))

        with open(os.path.join(options['data_dir'], 'routes.csv')) as f:
            csv_reader = csv.DictReader(f)
            for row in tqdm(csv_reader):

                if row['airline_id'].isdigit():
                    airline = Airline.objects.get(openflights_id=row['airline_id'])
                else:
                    airline = None

                if row['equipment'].isalnum():
                    try:
                        equipment = Equipment.objects.get(iata=row['equipment'])
                    except Exception:
                        equipment = None
                else:
                    equipment = None

                if row['source_airport'].isalnum():
                    try:
                        source_airport = Airport.objects.get(iata=row['source_airport'])
                    except Exception:
                        source_airport = None
                else:
                    source_airport = None

                if row['dest_airport'].isalnum():
                    try:
                        dest_airport = Airport.objects.get(iata=row['dest_airport'])
                    except Exception:
                        dest_airport = None
                else:
                    dest_airport = None

                route = Route(
                    airline=airline,
                    equipment=equipment,
                    source=source_airport,
                    dest=dest_airport,
                    stops=row['stops'],
                    codeshare=row['codeshare'] == 'Y', )

                route.save()
