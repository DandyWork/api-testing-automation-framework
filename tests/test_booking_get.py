import pytest


@pytest.mark.booking
def test_get_booking_by_id(
    booking_api,
    created_booking
):

    booking_id = created_booking["id"]


    response = booking_api.get_booking_by_id(
        booking_id
    )


    assert response.status_code == 200


    assert response.json["firstname"] == (
        created_booking["payload"]["firstname"]
    )


    assert response.json["lastname"] == (
        created_booking["payload"]["lastname"]
    )