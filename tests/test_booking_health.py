import pytest

@pytest.mark.booking
def test_get_booking_list(booking_api):

    response = booking_api.get_booking()

    assert response.status_code == 200