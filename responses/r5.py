import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
         timeout=5
    )
    response.raise_for_status()
    data = response.json()
    print(data["name"])
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError:
    print("HTTP error occurred")