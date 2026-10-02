import json

with open("person.json", "r") as file:
    person = json.load(file)

print(person)
print(person["name"])
print(person["skills"])