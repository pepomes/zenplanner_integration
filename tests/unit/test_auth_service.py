import pytest
import requests_mock
from zenplanner.services import AuthService

def test_authenticate_success():
    with requests_mock.Mocker() as m:
        m.post('https://memberappv220.zenplanner.com/auth/v1/login', json={"token": "access", "lockoutDate": 3600, "refreshToken": "refresh", "token_type": "bearer"})
        auth_service = AuthService("client_id", "client_secret")
        access_token, expires = auth_service.authenticate()
        assert access_token == "access"
        assert expires == 3600

def test_authenticate_failure():
    with requests_mock.Mocker() as m:
        m.post('https://memberappv220.zenplanner.com/auth/v1/login', status_code=401)
        auth_service = AuthService("client_id", "client_secret")
        with pytest.raises(Exception) as e:
            auth_service.authenticate()
        assert str(e.value) == "Failed to authenticate: b''"
