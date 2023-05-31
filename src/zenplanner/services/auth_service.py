import requests
from zenplanner import config
from dotenv import load_dotenv
import os

# load up all entries as environment variables
load_dotenv()
class AuthService:
    def __init__(self, client_id=None, client_secret=None):
        self.base_url = config.BASE_URL
        self.client_id = client_id or os.getenv("CLIENT_ID")
        self.client_secret = client_secret or os.getenv("CLIENT_SECRET")
        self._refresh_token = None


    def authenticate(self):
        auth_url = f"{self.base_url}/auth/v1/login"

        body = {
            "username": self.client_id,
            "password": self.client_secret,
            "grant_type": "client_credentials",
            "requiredRoles": ["PORTAL"],
        }

        response = requests.post(auth_url, json=body, verify=False)

        if response.status_code != 200:
            raise Exception(f"Failed to authenticate: {response.content}")

        data = response.json()
        print(data)
        self.refresh_token = data['refreshToken']

        return data['token'], data['lockoutDate']
