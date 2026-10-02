import requests

new_post = {
    "title": "AI Engineer Journey",
    "body": "Learning Python and APIs",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post)
print(response.status_code)
data = response.json()
print(data)
print(data["title"])
print(data["id"])