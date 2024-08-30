import json
import requests
from datetime import datetime
import os

today = datetime.now()
EXERSICE_API_ENDPOINT = os.environ["NX_ENDPOINT"]
EXCEL_SHEET_API_ENDPOINT = os.environ["SHEET_ENDPOINT"]
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]
# print(TOKEN)
date_format = today.strftime("%d/%m/%G")
time_format = today.strftime("%X")
# print(date_format,time_format)
headers = {
    'Content-Type': 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exersice you did:")
}

response = requests.post(url=EXERSICE_API_ENDPOINT, data=json.dumps(parameters), headers=headers)
response.raise_for_status()
Exercise = response.json()["exercises"]
# print(Exercise)
EXCEL_HEADER = {
    "Authorization": f"Bearer {TOKEN}"
}
for exercise in Exercise:
    EXCEL_PARAMETERS = {
        "workout": {
            "date": date_format,
            "time": time_format,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    excel_response = requests.post(url=EXCEL_SHEET_API_ENDPOINT, json=EXCEL_PARAMETERS, headers=EXCEL_HEADER)
    # excel_response.raise_for_status()
    print(excel_response.text)
