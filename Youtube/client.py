import requests
from urllib import parse
from urllib import request as req
from pathlib import Path

from .class_mapper import FUNCTION_CLASS_METHOD_MAP

from .activities import Activities
from .captions import Captions
from .channel import Channel
from .comments import Comment
from .playlist import Playlist
from .search import Search
from .video import Video

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

    @classmethod
    def get_endpoint_params(cls, method_name: str, **kwargs) -> tuple:
        """
        Given the endpoint class and it's functions name, calls the function

        :param method_name:
            :requred:
            desc: method name listed in class_mapper.py
            :type str:

        :param kwargs:
            :required:
            desc: parameters values for the request
            :type dict:

        :return endpoint name and parameters for request:
            :rtype tuple:
        """
        endpoint_content: dict = FUNCTION_CLASS_METHOD_MAP[method_name]
        endpoint_class: object = eval(endpoint_content.get('class'))()
        endpoint_method: str = endpoint_content.get('class_method')

        return getattr(
            endpoint_class,
            endpoint_method)(**kwargs)

    def request(self, method_name: str, **kwargs) -> requests.Response:
        """
        Given method name from class_mapper.py and params returns the request response in json format.

        :param method_name:
            :requred:
            desc: method name listed in class_mapper.py
            :type str:

        :param kwargs:
            :required:
            desc: parameters values for the request
            :type dict:

        :return structured response of request:
            :rtype dict:
        """
        endpoint, params = self.get_endpoint_params(method_name, **kwargs)
        params['key'] = self._key

        return requests.get(self.base_url + endpoint + "?" + parse.urlencode(params))