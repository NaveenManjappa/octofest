# Test data for populating the octofit_db database

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
    {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
]

test_activities = [
    {"username": "thundergod", "type": "Cycling", "duration": 60},
    {"username": "metalgeek", "type": "Crossfit", "duration": 120},
    {"username": "zerocool", "type": "Running", "duration": 90},
    {"username": "crashoverride", "type": "Strength", "duration": 30},
    {"username": "sleeptoken", "type": "Swimming", "duration": 75},
]

test_leaderboard = [
    {"username": "thundergod", "score": 100},
    {"username": "metalgeek", "score": 90},
    {"username": "zerocool", "score": 95},
    {"username": "crashoverride", "score": 85},
    {"username": "sleeptoken", "score": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
