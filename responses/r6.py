# Day 11 Challenge — .env + GET API
#
# Step 1: Create a .env file containing:
# API_URL=https://jsonplaceholder.typicode.com
#
# Step 2: Python task
#
# 1. Import os, requests, and load_dotenv.
# 2. Load the .env file.
# 3. Get API_URL using os.getenv().
# 4. Create the URL for user 1 by adding /users/1.
# 5. Send a GET request to that URL.
# 6. Convert the response to JSON.
# 7. Print the user's name and email.
#
# Expected flow:
#
# .env
#   ↓
# API_URL
#   ↓
# os.getenv()
#   ↓
# API_URL + "/users/1"
#   ↓
# GET request
#   ↓
# JSON
#   ↓
# name + email
#
# Do not use POST for this exercise.


import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("MY_NAME")
print(api_key)
api_url = os.getenv("API_URL")
print(api_url)
url = api_url + "/users/1"
get_response = requests.get(url)
data = get_response.json()
print(data["name"])
print(data["email"])
