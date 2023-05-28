import requests

class AuthService:
    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self._refresh_token = None

    def authenticate(self, scope):
        auth_url = f"{self.base_url}/auth"

        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": scope
        }

        response = requests.post(auth_url, json=body)

        if response.status_code != 200:
            raise Exception(f"Failed to authenticate: {response.content}")

        data = response.json()

        self.refresh_token = data['refresh_token']

        return data['access_token'], data['expires']

    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value 
    
    def refresh_auth_token(self):
        if not self._refresh_token:
            raise Exception("No refresh token found")

        auth_url = f"{self.base_url}/auth"

        body = {
            "client_id": self.client_id,
            "grant_type": "refresh_token",
            "refresh_token": self._refresh_token
        }

        response = requests.post(auth_url, json=body)

        if response.status_code != 200:
            raise Exception(f"Failed to refresh token: {response.content}")

        data = response.json()

        self._refresh_token = data['refresh_token']

        return data['access_token'], data['expires']

