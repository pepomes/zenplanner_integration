import pytest
from zenplanner.services import AuthService
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize AuthService
auth_service = AuthService()

def test_authenticate_success():
    access_token, expires = auth_service.authenticate()
    
    # Check that access token and expiration are not None
    assert access_token is not None


