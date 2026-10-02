import requests

headers = {
    "Accept": "application/json"
}
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
    headers=headers
)
data = response.json()
print(data["name"])
