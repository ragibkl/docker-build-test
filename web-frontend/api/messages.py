import os
import json
import requests


API_MESSAGES_BASE_URL = os.environ.get("API_MESSAGES_BASE_URL", "http://localhost:5001")


def get_message():
    api_url = f"{API_MESSAGES_BASE_URL}/api/message"
    response = requests.get(api_url)

    return json.loads(response.text)
