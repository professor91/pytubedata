import requests
from .exceptions import UnauthorizedException, RateLimitExceededException


class APIRequest:
    BASE_URL = "https://www.googleapis.com/youtube/v3/"

    def __init__(self, api_key):
        self.api_key = api_key

    def make_request(self, endpoint: str, params: dict = None) -> dict:
        """
        """
        url = APIRequest.BASE_URL + endpoint
        params = params or {}
        params["key"] = self.api_key

        response = requests.get(url, params=params)

        if response.status_code == 401:
            raise UnauthorizedException("Invalid or missing API key.")
        elif response.status_code == 403:
            raise RateLimitExceededException("API rate limit exceeded. Please try again later.")
        elif response.status_code != 200:
            raise Exception(f"Failed to fetch data from the API. Status code: {response.status_code}")

        data = response.json()
        return data
