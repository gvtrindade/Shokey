import json

from app.entities.Profile import Profile


def get_profiles():
    with open("src/profiles.json", "r") as f:
        d = json.loads(f.read())

    profiles = []
    for data in d.values():
        profiles.append(Profile(data))

    return profiles


def get_profile_index(profiles, name):
    for i, profile in enumerate(profiles):
        if profile.name == name:
            return i
