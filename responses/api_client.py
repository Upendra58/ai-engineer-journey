import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_url = os.getenv("API_URL")

headers = {
    "Accept": "application/json"
}
def get_user(user_id):
    url = api_url + "/users/"+ str(user_id)
    try:
        response = requests.get(
            url,
            headers = headers,
            timeout = 5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Requested Time out")
        return None
    except requests.exceptions.HTTPError:
        print("HTTP Error occured")
        return None
    except requests.exceptions.ConnectionError:
        print("Could not connect")
        return None
user = get_user(1)
if user:
    print(user["name"])
    print(user["email"])
else:
    print("Could not retrive data")