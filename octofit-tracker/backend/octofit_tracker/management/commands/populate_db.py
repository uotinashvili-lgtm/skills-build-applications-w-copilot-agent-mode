from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn.client['octofit_db']
        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create teams
        teams = [
            {"name": "Team Marvel"},
            {"name": "Team DC"}
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Create users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team_id": team_ids[0]},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team_id": team_ids[0]},
            {"name": "Batman", "email": "batman@dc.com", "team_id": team_ids[1]},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team_id": team_ids[1]},
        ]
        db.users.insert_many(users)
        db.users.create_index("email", unique=True)

        # Create activities
        activities = [
            {"user": "spiderman@marvel.com", "activity": "Running", "duration": 30},
            {"user": "ironman@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "batman@dc.com", "activity": "Swimming", "duration": 60},
            {"user": "wonderwoman@dc.com", "activity": "Yoga", "duration": 50},
        ]
        db.activities.insert_many(activities)

        # Create workouts
        workouts = [
            {"user": "spiderman@marvel.com", "workout": "Pushups", "reps": 100},
            {"user": "ironman@marvel.com", "workout": "Situps", "reps": 150},
            {"user": "batman@dc.com", "workout": "Pullups", "reps": 80},
            {"user": "wonderwoman@dc.com", "workout": "Squats", "reps": 120},
        ]
        db.workouts.insert_many(workouts)

        # Create leaderboard
        leaderboard = [
            {"user": "spiderman@marvel.com", "points": 120},
            {"user": "ironman@marvel.com", "points": 140},
            {"user": "batman@dc.com", "points": 130},
            {"user": "wonderwoman@dc.com", "points": 135},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
