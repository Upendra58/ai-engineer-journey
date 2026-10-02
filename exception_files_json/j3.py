import json

person = {
    "name": "Upendra",
    "age": 25,
    "role": "AI Engineer",
    "skills": ["Python", "JavaScript", "API"]
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)