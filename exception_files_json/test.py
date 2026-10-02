import json

try:
    with open("profile.json", "r") as file:
        print (json.load(file))
except FileNotFoundError:
    print("No file found")