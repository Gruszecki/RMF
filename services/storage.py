from datetime import datetime

import requests

import secrets_handler


REGION = ''  # If German region, set this to an empty string: ''
STORAGE_ZONE_NAME = 'rate-my-fart'
FILENAME_EXTENSION = 'mp3'
ACCESS_KEY = secrets_handler.BUNNY_API_KEY


def save_audio(filepath: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_") + str(int(datetime.now().microsecond / 1000)).zfill(3)
    FILENAME = f"fart_{timestamp}.{FILENAME_EXTENSION}"
    base_url = "storage.bunnycdn.com"
    if REGION:
        base_url = f"{REGION}.{base_url}"

    url = f"https://{base_url}/{STORAGE_ZONE_NAME}/{FILENAME}"

    headers = {
        "AccessKey": ACCESS_KEY,
        "Content-Type": "application/octet-stream",
        "accept": "application/json"
    }

    with open(filepath, 'rb') as file_data:
        response = requests.put(url, headers=headers, data=file_data)

    return response.status_code, FILENAME
