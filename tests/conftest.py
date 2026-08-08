import pytest
from framework.api_client import APIClient
from config.settings import BASE_URL
from apis.booking_api import BookingAPI
from apis.auth_api import AuthAPI
from utils.test_data_reader import load_test_data
from config.settings import USERNAME, PASSWORD


@pytest.fixture
def api_client():

    return APIClient(
        BASE_URL
    )


@pytest.fixture
def booking_api(api_client):

    return BookingAPI(
        api_client
    )


@pytest.fixture
def auth_api(api_client):

    return AuthAPI(
        api_client
    )

@pytest.fixture
def created_booking(booking_api):

    data = load_test_data(
        "booking_data.json"
    )

    response = booking_api.create_booking(
        data["valid_booking"]
    )

    assert response.status_code == 200

    return {
        "id": response.json["bookingid"],
        "payload": data["valid_booking"]
    }

@pytest.fixture
def auth_token(auth_api):

    response = auth_api.login(
        USERNAME,
        PASSWORD
    )

    assert response.status_code == 200
    assert "token" in response.json, (
        f"Authentication failed: {response.json}"
    )

    return response.json["token"]