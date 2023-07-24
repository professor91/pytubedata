import requests
from pytubedata.exceptions import UnauthorizedException
from pytubedata.config import MAX_RESULTS

class APIRequest:
    BASE_URL = "https://www.googleapis.com/youtube/v3/"

    def __init__(self, api_key, **kwargs):
        self.api_key = api_key
        self.max_results: int = kwargs.get('max_results', MAX_RESULTS)

    def make_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Make HTTP requests to YouTube Data API
        """
        url = APIRequest.BASE_URL + endpoint
        params = params or {}
        params["key"] = self.api_key

        data = self._handle_pagination(url=url, params=params)

        return {
            'items': data
        }

    def _handle_pagination(self, url: str, params: dict) -> list[dict]:
        """
        Fetch multiple pages
        """
        all_data = []

        while True:
            response = requests.get(url=url, params=params)
            self.handle_errors(status_code=response.status_code)

            response_data: dict = response.json()
            items = response_data.get("items", [])
            all_data.extend(items)

            next_page_token = response_data.get("nextPageToken")

            if len(all_data)+5 > self.max_results:
                break

            if not next_page_token:
                break

            params["pageToken"] = next_page_token
            # print(next_page_token)

        return all_data

    @staticmethod
    def handle_errors(status_code: int):
        """
        API error handler
        """
        if status_code == 400:
            raise UnauthorizedException("Invalid or missing API key.")
        # elif status_code == 403:
        #     raise RateLimitExceededException("API rate limit exceeded. Please try again later.")
        elif status_code != 200:
            raise Exception(f"Failed to fetch data from the API. Status code: {status_code}")
