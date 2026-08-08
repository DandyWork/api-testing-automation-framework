import pytest

from utils.test_data_reader import load_test_data


negative_data = load_test_data(
    "booking_negative_data.json"
)


@pytest.mark.booking
@pytest.mark.parametrize(
    "scenario",
    [
        "missing_firstname",
        "missing_lastname"
    ]
)
def test_create_booking_negative(
    booking_api,
    scenario
):
    test_case = negative_data[scenario]

    response = booking_api.create_booking(
        test_case["payload"]
    )

    assert response.status_code == (
        test_case["expected_status"]
    )

@pytest.mark.booking
@pytest.mark.xfail(
    reason="API accepts invalid datatype for totalprice"
)
def test_create_booking_invalid_price_type(
    booking_api
):

    payload = negative_data[
        "invalid_price_type"
    ]


    response = booking_api.create_booking(
        payload
    )


    assert response.status_code == 500