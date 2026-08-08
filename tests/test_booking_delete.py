import pytest


@pytest.mark.booking
def test_delete_booking(
    booking_api,
    created_booking,
    auth_token
):

    booking_id = created_booking["id"]


    response = booking_api.delete_booking(
        booking_id,
        auth_token
    )


    assert response.status_code == 201

    get_response = booking_api.get_booking_by_id(
    booking_id
    )

    assert get_response.status_code == 404