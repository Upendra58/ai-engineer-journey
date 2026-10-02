import json

person = {
    "name" : "Upendra",
    "age"  : 25,
    "role" : "AI Engineer",
    "skills": ["Python", "API", "JS"]
}

data = json.dumps(person)
print(data)