from django.core.management.base import BaseCommand
from athletes.models import Athlete
import csv
import os

PATH = os.path.dirname(os.path.abspath(__file__))
ATHLETES_CSV = PATH + '/athletes.csv'

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_athletes_from_csv()
    
    def create_athletes_from_csv(self):
        with open(ATHLETES_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                # Athlete.objects.get_or_create()
                print(row)