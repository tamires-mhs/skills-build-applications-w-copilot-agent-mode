from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='test1234', team=team)
        self.assertEqual(user.email, 'test@test.com')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='test1234', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, calories=100)
        self.assertEqual(activity.type, 'run')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='test1234', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=123)
        self.assertEqual(leaderboard.points, 123)
