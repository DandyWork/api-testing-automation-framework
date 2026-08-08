class APIResponse:

    def __init__(self, response):

        self.response = response
        self.status_code = response.status_code
        self.headers = response.headers
        self._json = None


    @property
    def json(self):

        if self._json is None:
            self._json = self.response.json()

        return self._json


    @property
    def text(self):

        return self.response.text


    @property
    def elapsed_time(self):

        return self.response.elapsed.total_seconds()