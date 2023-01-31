import requests
from urllib import parse
from pathlib import Path
import copy

from .api_mapper import API_MAPPER
from .parser import Parser


class Auth:
    __BASE_URL = "https://www.googleapis.com/youtube/v3"

    def __init__(self):
        self.__key = self._get_secret_key()

    @property
    def base_url(self) -> str:
        return self.__BASE_URL

    @property
    def key(self) -> str:
        return self.__key

    def _get_secret_key(self) -> str:
        """
        Reads the key from `secret.yml` file and calls self._verifi_key()

        :return API key from `secret.yml` file:
        """
        CURRENT_WORKING_DIRECTORY: Path = Path().cwd()
        SECRET_FILE: Path = CURRENT_WORKING_DIRECTORY / 'secret.yml'

        key: str = SECRET_FILE.read_text()

        if not key:
            raise ValueError("Google API key is required please visit http://code.google.com/apis/console")

        if self._verify_key(key):
            raise ValueError('The API Key is invalid')
        else:
            return key

    def _verify_key(self, key: str) -> bool:
        """
        Given the YouTube API key, verifies if it's correct

        :param key:
            :required:
            desc: YouTube Data API key. Visit http://code.google.com/apis/console to create one
            :type str:

        :return bool if key is authentic:
            :rtype str:
        """

        res = requests.get(self.base_url + 'search' + '?' + 'key' + key + 'part' + 'snippet')

        if res.status_code != 200:
            return False
        else:
            return True


class Client(Auth):
    """
    The YouTube Data API handles the keys and methods to access data from the YouTube Data API
    """

    def __init__(self):
        super().__init__()
        self._key = self.key

        if self._key:
            print('Client is ready')

    @staticmethod
    def __update_id(params: dict, id: str) -> dict:
        try:
            params.update({
                list(filter(lambda p: "Id" in p, params.keys()))[0]: id,
            })
        except IndexError:
            params.update({
                'id': id
            })

        return params

    def request(self,
                method_name: str,
                id: str = None,
                max_results: int = 10,
                published_before: str = None,
                published_after: str = None,
                region_code: str = None,
                parse_result: bool = True,
                ) -> list:
        """

        :param method_name:
        :param id:
        :param max_results:
        :param published_before:
        :param published_after:
        :param region_code:
        :param parse_result:
        :return:
        """
        endpoint_content: dict = copy.deepcopy(API_MAPPER[method_name])
        endpoint: str = endpoint_content["endpoint"]
        params: dict = endpoint_content["params"]

        if published_before and method_name == 'activity':
            params.update({
                "publishedBefore": published_before,
            })
        if published_after and method_name == 'activity':
            params.update({
                "publishedAfter": published_after,
            })
        if region_code and (method_name == 'activity' or method_name == 'video_by_id'):
            params.update({
                "regionCode": region_code,
            })
        params.update({
            "maxResults": max_results
        })

        params = Client.__update_id(params=params, id=id)

        params.update({
            "key": self._key,
        })

        data: list = self.__send_request(
            endpoint=endpoint,
            params=params,
        )

        if parse_result:
            parse_method = endpoint_content['parse_function']
            return getattr(Parser, parse_method)(data)
        else:
            return data

    def __send_request(
            self, endpoint: str = None,
            params: dict = None,
            **kwargs) -> list:
        """
        Given method name from api_mapper.py and params returns the request response in json format.

        :return structured response of request:
            :rtype dict:
        """

        if 'next_page_token' in kwargs.keys():
            params.update({
                'pageToken': kwargs.get('next_page_token')
            })

        response = requests.get(self.base_url + endpoint + "?" + parse.urlencode(params))

        data: list = []

        if 'nextPageToken' in response.json().keys():
            data.extend(
                self.__send_request(
                    endpoint=endpoint,
                    params=params,
                    next_page_token=response.json()['nextPageToken']
                )
            )
        # Todo- error handling for api responses
        data.extend(response.json()['items'])

        return data
