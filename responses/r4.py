import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    response.raise_for_status()
    data = response.json()
    print(data["name"])
except requests.exceptions.HTTPError:
    print("User request failed")