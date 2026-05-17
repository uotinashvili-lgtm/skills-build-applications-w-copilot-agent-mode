from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

    def test_user_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        self.assertEqual(str(user), "test@example.com")

    def test_activity_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        activity = Activity.objects.create(user=user, activity="Running", duration=30)
        self.assertEqual(str(activity), "test@example.com - Running")

    def test_workout_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        workout = Workout.objects.create(user=user, workout="Pushups", reps=100)
        self.assertEqual(str(workout), "test@example.com - Pushups")

    def test_leaderboard_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=50)
        self.assertEqual(str(leaderboard), "test@example.com - 50")
