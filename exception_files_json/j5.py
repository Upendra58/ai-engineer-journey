import json

profile = {
     "name" : "Upendra",
        "age"  : 25,
        "role" : "AI Engineer",
        "skills": ["Python", "API", "JavaScript"]
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r") as file:
    print(json.load(file))
print(profile["name"])
print(profile["skills"])
print(profile["role"])