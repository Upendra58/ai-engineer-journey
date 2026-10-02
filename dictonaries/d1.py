person = {
    "name": "Upendra",
    "age": 25,
    "city": "Bangalore",
    "role": "Software Engineer"
}
person["age"] = 26
person["role"] = "AI Engineer"
person["experience"] = 3
del person["city"]

for key,value in person.items():
    print(key,":", value)