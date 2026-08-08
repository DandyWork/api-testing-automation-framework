import pytest
from utils.test_data_reader import load_test_data

auth_data = load_test_data(
    "auth_data.json"
)

@pytest.mark.auth
def test_login_success(auth_api):

    user = auth_data["valid_user"]


    response = auth_api.login(
        user["username"],
        user["password"]
    )


    assert response.status_code == user["expected_status"]

    assert "token" in response.json

@pytest.mark.auth
@pytest.mark.parametrize(
    "scenario",
    [
        "invalid_password",
        "missing_username",
        "missing_password"
    ]
)
def test_login_negative(auth_api, scenario):

    user = auth_data[scenario]


    response = auth_api.login(
        user["username"],
        user["password"]
    )

    print(response.json)
    assert response.status_code == user["expected_status"]

    assert response.json["reason"] == user["expected_message"]