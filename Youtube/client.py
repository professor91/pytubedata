import requests
from urllib import parse
from pathlib import Path

from .api_mapper import API_MAPPER


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

    def request(self,
                method_name: str,
                id: str = None,
                max_results: int = None,
                published_before: str = None,
                published_after: str = None,
                region_code: str = None
                ) -> requests.Response:
        """
        Given method name from api_mapper.py and params returns the request response in json format.

        :param region_code:
        :param published_after:
        :param published_before:
        :param method_name:
            :requred:
            desc: method name listed in api_mapper.py
            :type str:

        :param id:
        :param max_results:

        :return structured response of request:
            :rtype dict:
        """
        endpoint_content: dict = API_MAPPER[method_name]
        endpoint: str = endpoint_content["endpoint"]
        params: dict = endpoint_content["params"]

        if published_before:
            params.update({
                "publishedBefore": published_before,
            })
        if published_after:
            params.update({
                "publishedAfter": published_after,
            })
        if region_code:
            params.update({
                "regionCode": region_code,
            })
        if max_results:
            params.update({
                "maxResults": max_results
            })

        params.update({
            list(filter(lambda p: "Id" in p, params.keys()))[0]: id,
        })

        params.update({
            "key": self._key,
        })

        for k, v in dict(params).items():
            if v is None:
                del params[k]

        return requests.get(self.base_url + endpoint + "?" + parse.urlencode(params))
