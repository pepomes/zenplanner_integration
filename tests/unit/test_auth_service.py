import pytest
import requests_mock
from zenplanner.services import AuthService

def test_authenticate_success():
    with requests_mock.Mocker() as m:
        m.post('https://memberappv220.zenplanner.com/auth', json={"access_token": "access", "expires": 3600, "refresh_token": "refresh", "token_type": "bearer"})
        auth_service = AuthService("client_id", "client_secret")
        access_token, expires = auth_service.authenticate("scope")
        assert access_token == "access"
        assert expires == 3600

def test_authenticate_failure():
    with requests_mock.Mocker() as m:
        m.post('https://memberappv220.zenplanner.com/auth', status_code=401)
        auth_service = AuthService("client_id", "client_secret")
        with pytest.raises(Exception) as e:
            auth_service.authenticate("scope")
        assert str(e.value) == "Failed to authenticate: b''"

def test_refresh_token_success():
    with requests_mock.Mocker() as m:
        m.post('https://memberappv220.zenplanner.com/auth', json={"access_token": "access_new", "expires": 3600, "refresh_token": "refresh_new", "token_type": "bearer"})
        auth_service = AuthService("client_id", "client_secret")
        auth_service.refresh_token = "refresh"
        access_token, expires = auth_service.refresh_auth_token()
        assert access_token == "access_new"
        assert expires == 3600

def test_refresh_token_failure():
    with requests_mock.Mocker() as m:
        m.post('https://memberappv220.zenplanner.com/auth', status_code=401)
        auth_service = AuthService("client_id", "client_secret")
        auth_service.refresh_token = "refresh"
        with pytest.raises(Exception) as e:
            auth_service.refresh_auth_token()
        assert str(e.value) == "Failed to refresh token: b''"

def test_refresh_token_no_refresh_token():
    auth_service = AuthService("client_id", "client_secret")
    with pytest.raises(Exception) as e:
        auth_service.refresh_auth_token()
    assert str(e.value) == "No refresh token found"
