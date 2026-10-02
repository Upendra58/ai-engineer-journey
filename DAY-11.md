# Day 11 — Python APIs, Requests, Environment Variables & Error Handling

## Focus
Build a reusable Python API client using HTTP, `requests`, JSON, environment variables, headers, timeouts, and error handling.

## Completed
- HTTP request/response
- GET, POST, PUT, PATCH, DELETE concepts
- HTTP status codes
- Query parameters
- JSON request bodies
- `requests.get()` and `requests.post()`
- `response.json()`
- Headers
- `raise_for_status()`
- Timeouts
- `Timeout`, `HTTPError`, `ConnectionError`
- `.env`
- `python-dotenv`
- `os.getenv()`
- Reusable API functions
- `return` vs `print`
- Safe `None` handling

## Final Mini-Project
Created a reusable `get_user(user_id)` API client that loads the base URL from `.env`, builds the endpoint dynamically, sends a GET request, uses headers and a 5-second timeout, parses JSON, handles errors, and returns data or `None`.

## Final Pattern
```python
import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_url = os.getenv("API_URL")

headers = {
    "Accept": "application/json"
}

def get_user(user_id):
    url = api_url + "/users/" + str(user_id)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out")
        return None

    except requests.exceptions.HTTPError:
        print("HTTP error occurred")
        return None

    except requests.exceptions.ConnectionError:
        print("Could not connect to the API")
        return None
```

## Key Takeaways
- Keep configuration outside source code where possible.
- Always set network timeouts.
- Separate HTTP failures from network failures.
- Reusable functions should return data.
- Callers should handle failed requests safely.

## Assessment
**Day 11: 🟢 COMPLETE**

## Next
Day 12 — Python Project Structure + Logging + Testing
