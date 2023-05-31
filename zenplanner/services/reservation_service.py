import requests
from zenplanner import config
from dotenv import load_dotenv
import os
import json

# load up all entries as environment variables
load_dotenv()

class ReservationService:
    def __init__(self, bearer_token, person_id=None):
        self.base_url = config.BASE_URL
        self.bearer_token = bearer_token
        self.person_id = person_id or os.getenv("PERSON_ID")

    def get_reservations(self, person_id=None):
        url = f"{self.base_url}/calendars/reservations"

        headers = {
            "Accept": "application/json; charset=utf-8",
            "Authorization": f"Bearer {self.bearer_token}",
            "partitionid": "67294411-AE54-4CBF-B32B-5090CDBF4A5E",
            "componentversionid": "8D052224-6C15-4986-BF65-4ED646EAE8BF",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "x-auth-refresh": f"",
            "User-Agent": "Zen%20Planner/2.4.37 CFNetwork/1404.0.5 Darwin/22.3.0",
            "Content-Type": "application/json",
            "appsource": "MEMBER_APP",
        }

        data = {
            "personId": person_id
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Convert response to JSON format
        reservations = response.json()

        return reservations
