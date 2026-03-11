from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Limpa dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Cria usuários
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@dc.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)

        # Cria atividades
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        Activity.objects.create(user=clark, type='run', duration=50, calories=450)

        # Cria treinos
        Workout.objects.create(name='Full Body', description='Treino completo', suggested_for='Marvel')
        Workout.objects.create(name='Cardio Hero', description='Cardio intenso', suggested_for='DC')

        # Cria leaderboard
        Leaderboard.objects.create(user=tony, points=1000)
        Leaderboard.objects.create(user=steve, points=900)
        Leaderboard.objects.create(user=bruce, points=950)
        Leaderboard.objects.create(user=clark, points=1100)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
