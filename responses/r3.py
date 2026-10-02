import requests

params = {

    "id" : 3
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    params = params
)

data = response.json()
print(data)
