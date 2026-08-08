class BookingAPI:

    def __init__(self, api_client):
        self.api_client = api_client


    def get_booking(self):

        return self.api_client.get(
            "/booking"
        )


    def get_booking_by_id(self, booking_id):

        return self.api_client.get(
            f"/booking/{booking_id}"
        )


    def create_booking(self, payload):

        return self.api_client.post(
            "/booking",
            json=payload
        )

    def update_booking(
        self,
        booking_id,
        payload,
        token
    ):

        headers = {
            "Cookie": f"token={token}"
        }

        return self.api_client.put(
            f"/booking/{booking_id}",
            json=payload,
            headers=headers
        )

    def delete_booking(
        self,
        booking_id,
        token
    ):

        headers = {
            "Cookie": f"token={token}"
        }


        return self.api_client.delete(
            f"/booking/{booking_id}",
            headers=headers
        )