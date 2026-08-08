class AuthAPI:

    def __init__(self, api_client):

        self.api_client = api_client


    def login(self, username, password):

        payload = {
            "username": username,
            "password": password
        }

        return self.api_client.post(
            "/auth",
            json=payload
        )