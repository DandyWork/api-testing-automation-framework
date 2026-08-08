import requests
from framework.api_response import APIResponse
from utils.logger import get_logger

class APIClient:

    def __init__(self, base_url):

        self.base_url = base_url
        self.logger = get_logger(__name__)


    def _request(self, method, endpoint, **kwargs):

        url = self.base_url + endpoint

        self.logger.info(
            f"{method} {url}"
        )

        if "json" in kwargs:
            self.logger.info(
                f"Request Body: {kwargs['json']}"
            )


        response = requests.request(
            method,
            url,
            **kwargs
        )


        self.logger.info(
            f"Status Code: {response.status_code}"
        )

        self.logger.info(
            f"Response Time: {response.elapsed.total_seconds()}s"
        )


        return APIResponse(response)



    def get(self, endpoint, **kwargs):

        return self._request(
            "GET",
            endpoint,
            **kwargs
        )


    def post(self, endpoint, **kwargs):

        return self._request(
            "POST",
            endpoint,
            **kwargs
        )


    def put(self, endpoint, **kwargs):

        return self._request(
            "PUT",
            endpoint,
            **kwargs
        )


    def delete(self, endpoint, **kwargs):

        return self._request(
            "DELETE",
            endpoint,
            **kwargs
        )