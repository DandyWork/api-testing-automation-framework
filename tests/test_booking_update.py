import pytest

from utils.test_data_reader import load_test_data
from utils.schema_validator import validate_schema


booking_data = load_test_data(
    "booking_data.json"
)


@pytest.mark.booking
def test_update_booking(
    booking_api,
    created_booking,
    auth_token
):

    booking_id = created_booking["id"]


    payload = booking_data["updated_booking"]


    response = booking_api.update_booking(
        booking_id,
        payload,
        auth_token
    )

    validate_schema(
        response.json,
        "schemas/booking_detail_schema.json"
    )
    
    assert response.status_code == 200


    assert response.json["firstname"] == (
        payload["firstname"]
    )


    assert response.json["lastname"] == (
        payload["lastname"]
    )


    assert response.json["totalprice"] == (
        payload["totalprice"]
    )