import pytest
from utils.schema_validator import validate_schema

@pytest.mark.booking
def test_get_booking_list(booking_api):

    response = booking_api.get_booking()

    validate_schema(
        response.json,
        "schemas/booking_list_schema.json"
    )

    assert response.status_code == 200