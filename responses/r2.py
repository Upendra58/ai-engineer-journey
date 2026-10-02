import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/9999")

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data["name"])
    print(data["email"])
elif response.status_code == 404:
    print("User not found")
else:
    print("Request Failed")