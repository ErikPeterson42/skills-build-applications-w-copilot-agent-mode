from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Enhanced test users
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_brown', email='bob@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Enhanced test teams
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3, user4)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration='00:30:00')
        Activity.objects.create(user=user2, activity_type='Cycling', duration='01:00:00')

        # Additional test activities
        Activity.objects.create(user=user3, activity_type='Swimming', duration='00:45:00')
        Activity.objects.create(user=user4, activity_type='Hiking', duration='02:00:00')

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Additional test leaderboard entries
        Leaderboard.objects.create(user=user3, score=200)
        Leaderboard.objects.create(user=user4, score=250)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start your day.')
        Workout.objects.create(name='HIIT', description='High-Intensity Interval Training for fat burning.')

        # Additional test workouts
        Workout.objects.create(name='Evening Stretch', description='A calming stretch routine to end your day.')
        Workout.objects.create(name='Strength Training', description='Build muscle with this strength-focused workout.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data for'))
