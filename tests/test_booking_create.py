import pytest
from utils.test_data_reader import load_test_data
from utils.schema_validator import validate_schema


booking_data = load_test_data(
    "booking_data.json"
)

@pytest.mark.booking
def test_create_booking_success(booking_api):

    payload = booking_data["valid_booking"]


    response = booking_api.create_booking(
        payload
    )


    assert response.status_code == 200


    response_body = response.json

    validate_schema(
        response_body,
        "schemas/booking_schema.json"
    )

    assert "bookingid" in response_body


    assert response_body["booking"]["firstname"] == payload["firstname"]

    assert response_body["booking"]["lastname"] == payload["lastname"]

    assert response_body["booking"]["totalprice"] == payload["totalprice"]

    assert response_body["booking"]["depositpaid"] == payload["depositpaid"]