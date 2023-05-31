import pytest
import requests_mock
from zenplanner.services import ReservationService
import json

class TestReservationService:
    @pytest.fixture
    def service(self):
        bearer_token = 'test_token'
        person_id = '12345'
        return ReservationService(bearer_token, person_id)

    def test_init(self, service):
        assert service.bearer_token == 'test_token'
        assert service.person_id == '12345'

    def test_get_reservations(self, service):
        url = f"{service.base_url}/calendars/reservations"
        mock_response = {"reservation": "test_reservation"}

        with requests_mock.Mocker() as m:
            m.post(url, text=json.dumps(mock_response))
            reservations = service.get_reservations()
            assert reservations == mock_response

