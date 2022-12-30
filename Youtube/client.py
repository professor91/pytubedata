import requests
from urllib import parse
from urllib import request as req

from .class_mapper import FUNCTION_CLASS_METHOD_MAP

from .activities import activities
from .captions import captions
from .channel import channel
from .comments import comment
from .playlist import playlist
from .search import search
from .video import video

class client():
    """
    The Youtube Data API handles the keys and methods to access data from the YouTube Data API

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        if not key:
            raise ValueError("Google API key is required please visit http://code.google.com/apis/console")
        
        # if True and self.verify_key(params):
        #     raise ValueError('The API Key is invalid')

        self.key= key
        self.base_url= "https://www.googleapis.com/youtube/v3"

    @classmethod
    def get_endpoint_params(cls, method_name: str, **kwargs):

        endpoint_content: dict= FUNCTION_CLASS_METHOD_MAP[method_name]
        endpoint_class: object= eval(endpoint_content.get('class'))()
        endpoint_method: str= endpoint_content.get('class_method')

        return getattr(
                        endpoint_class,
                        endpoint_method)(**kwargs)

    def request(self, method_name, **kwargs):
        '''
        Given endpoint of API and params returns the request response in json format.

        params: required
            endpoint: from the given dictionary of endpoints in class_mapper.py
            type: str or list of str

            params: given when the function is called
            type: dict
        
        returns the request response in text format
                rtype: dict
        '''

        endpoint, params = self.get_endpoint_params(method_name, **kwargs)
        params['key'] = self.key

        res = requests.get(self.base_url + endpoint + "?" + parse.urlencode(params))

        return {
            "statusCode": res.status_code,
            "data": res.json()
        }

    def request_test(self, endpoint, params):
        '''
        Given endpoint of API and params returns the request response in text format.

        params: required
            endpoint: from the given dictionary of endpoints in class_mapper.py
            type: str or list of str

            params: given when the function is called
            type: dict

        returns the request response in text format
                rtype: text
        '''
        res= requests.get(self.base_url + FUNCTION_CLASS_METHOD_MAP[endpoint] + "?" + parse.urlencode(params))
        
        return res.text
    
    def request_url(self, endpoint, params):
        '''
        Given endpoint of API and params returns the request's parsed url.

        params: required
            endpoint: from the given dictionary of endpoints in class_mapper.py
            type: str or list of str

            params: given when the function is called
            type: dict

        returns the request's parsed url
                rtype: str
        '''
        return req.Request(self.base_url + FUNCTION_CLASS_METHOD_MAP[endpoint] + "?" + parse.urlencode(params)).get_full_url()
