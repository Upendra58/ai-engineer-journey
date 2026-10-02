import json
data = '{"name": "Upendra", "age": 25, "role": "AI Engineer"}'

person = json.loads(data)

print(person)
print(person["name"])