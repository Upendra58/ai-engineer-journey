import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

data = response.json()

print(response.status_code)
print(data["name"])
print(data["email"])