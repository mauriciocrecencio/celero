from django.core.management.base import BaseCommand
from athletes.models import Athlete, Athlete_instance
from events.models import Event
from sports.models import Sport, Game
from noc.models import Noc
import csv
import os

PATH = os.path.dirname(os.path.abspath(__file__))
ATHLETES_CSV = PATH + '/athletes.csv'
NOC_CSV = PATH + '/noc_regions.csv'


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('veio athlete')
        # self.create_games()
        # self.create_sports()
        # self.create_events()
        # self.create_nocs()
        # self.create_athletes()
        self.create_athletes_instances()

    def create_games(self):
        with open(ATHLETES_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                (game, game_created) = Game.objects.get_or_create(
                    name=row[8], year=row[9], season=row[10], city=row[11])
                if game_created:
                    print(f'{game.name} created')
                else:
                    print(f'{game.name} was already there')

    def create_sports(self):
        with open(ATHLETES_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                game = Game.objects.filter(name=row[8])
                (sport, sport_created) = Sport.objects.get_or_create(
                    name=row[12], game_id=game[0])
                if sport_created:
                    print(f'{sport.name} created')
                else:
                    print(f'{sport.name} was already there')

    def create_nocs(self):
        with open(NOC_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                noc, noc_created = Noc.objects.get_or_create(
                    name=row[0], region=row[1], notes=row[2])
                if noc_created:
                    print(f'{noc.name} created')
                else:
                    print(f'{noc.name} was already there')

    def create_events(self):
        with open(ATHLETES_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                sport = Sport.objects.filter(name=row[12])
                event, event_created = Event.objects.get_or_create(
                    name=row[13], sport_id=sport[0])
                if event_created:
                    print(f'{event.name} created')
                else:
                    print(f'{event.name} was already there')

    def create_athletes(self):
        with open(ATHLETES_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                noc = Noc.objects.filter(name=row[7])
                if len(noc) == 0:
                    noc = Noc.objects.get_or_create(
                        name=row[7], region=row[6], notes='default')
                athlete, athlete_created = Athlete.objects.get_or_create(
                    name=row[1], team=row[6], noc_id=noc[0].id, gender=row[2])
                if athlete_created:
                    print(f'{athlete.name} created')
                else:
                    print(f'{athlete.name} was already there')

    def create_athletes_instances(self):
        with open(ATHLETES_CSV) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                athlete = Athlete.objects.filter(name=row[1])
                event = Event.objects.filter(name=row[13])
                age = row[3]
                if age == 'NA':
                    age = 0
                athlete, athlete_created = Athlete_instance.objects.get_or_create(athlete_id=athlete[0], age=age, medal=row[14], height=row[4], weight=row[5])
                athlete.event_id.set(event)
                if athlete_created:
                    print(f'{athlete.medal} created')
                else:
                    print(f'{athlete.medal} was already there')
