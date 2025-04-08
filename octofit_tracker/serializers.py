from rest_framework import serializers

# Define serializers for users, teams, activity, leaderboard, and workouts
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.EmailField())

class ActivitySerializer(serializers.Serializer):
    user = serializers.EmailField()
    type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField(max_length=100)
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
