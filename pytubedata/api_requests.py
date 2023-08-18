"""
pytubedata.api_requests

This module provides a utility class to make HTTP requests to the YouTube Data API and handle pagination and errors.

Classes:
    APIRequest: Encapsulates all required functions to make HTTP requests to the YouTube Data API.
"""
import requests
from pytubedata.exceptions import UnauthorizedException
from pytubedata.config import MAX_RESULTS


class APIRequest:
    """
    A utility class to make HTTP requests to the YouTube Data API and handle pagination and errors.

    Attributes:
        BASE_URL (str): The base URL for the YouTube Data API.

    Methods:
        make_request(endpoint: str, params: dict = None, authorize: bool = False) -> dict:
            Make an HTTP request to the YouTube Data API.

        _handle_pagination(url: str, params: dict, headers: dict = None) -> list[dict]:
            Handle pagination in the API responses.

        handle_errors(status_code: int):
            Handle API errors in the response.

    Raises:
        UnauthorizedException: If the API key is invalid or missing.
        Exception: If the API request fails with a status code other than 200.

    TODO: handle rate limiting errors
    """
    BASE_URL = "https://www.googleapis.com/youtube/v3/"

    def __init__(self, api_key, access_token: str = None, **kwargs):
        """
        Initialize the APIRequest object.

        Args:
            api_key (str):  The API key to access the YouTube Data API.
                            You can get one from [Google Cloud Console](https://console.cloud.google.com/apis/dashboard).
            access_token (str, optional): An OAuth2 access token for authorized requests. Defaults to None.
            **kwargs: Additional keyword arguments.
        """
        self.api_key = api_key
        self.access_token = access_token

    def make_request(self, endpoint: str, params: dict = None, authorize: bool = False) -> dict:
        """
        Make an HTTP (GET) request to the YouTube Data API.

        Args:
            endpoint (str): The endpoint to be called.
            params (dict, optional): The parameters to be included in the request.
            authorize (bool, optional): Whether to include the access token for authenticated requests.

        Returns:
            dict: The JSON response from the API.

        Note: This function does not directly make the request but only prepares the params and headers,
                and depends on `_handle_pagination` method to get the request response
        """
        url = APIRequest.BASE_URL + endpoint
        params = params or {}
        """
        maxResults param in API params defines results per page -> range(0,50)

        self.max_results attribute tells client how many items to fetch
            it will decide if need to make additional requests using nextPageToken 
        """

        params["key"] = self.api_key
        headers = {'Authorization': f'Bearer {self.access_token}'} if authorize else None

        data: list[dict] = self._handle_pagination(url=url, params=params, headers=headers)

        return {
            'items': data
        }

    def _handle_pagination(self, url: str, params: dict, headers: dict = None) -> list[dict]:
        """
        Handle pagination in the API responses.

        Args:
            url (str): The URL of the API endpoint.
            params (dict): The parameters to be included in the request.
            headers (dict, optional): The headers to be included in the request.

        Returns:
            list[dict]: The list of data items retrieved from multiple API pages.

        Note: This function makes the actual api requests.
        """
        max_results = params.get('maxResults', MAX_RESULTS)
        all_data = []

        while True:
            response = requests.get(url=url, headers=headers, params=params)
            self.handle_errors(status_code=response.status_code)

            response_data: dict = response.json()
            items = response_data.get("items", [])
            all_data.extend(items)

            next_page_token = response_data.get("nextPageToken")

            if len(all_data)+5 > max_results:
                """
                Stop fetching more pages when the desired maximum number of results is reached.
                The YouTube Data API returns 5 results per page.
                """
                break

            if not next_page_token:
                break

            params["pageToken"] = next_page_token

        # TODO: can it cause memory overhead later on?
        return all_data[:max_results]

    @staticmethod
    def handle_errors(status_code: int):
        """
        Handle API errors in the response.

        Args:
            status_code (int): The HTTP status code of the API response.

        Raises:
            UnauthorizedException: If the API key is invalid or missing.
            Exception: If the API request fails with a status code other than 200.
        """
        if status_code == 400:
            raise UnauthorizedException("Invalid or missing API key.")
        # elif status_code == 403:
        #     raise RateLimitExceededException("API rate limit exceeded. Please try again later.")
        elif status_code != 200:
            raise Exception(f"Failed to fetch data from the API. Status code: {status_code}")
