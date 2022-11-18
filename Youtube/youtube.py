import requests
from urllib import parse
from urllib import request as req

from .endpoints import ENDPOINTS

class api():
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

    def request(self, endpoint, params):
        '''
        Given endpoint of API and params returns the request response in json format.

        params: required
            endpoint: from the given dictionary of endpoints in endpoints.py
            type: str or list of str

            params: given when the function is called
            type: dict
        
        returns the request response in text format
                rtype: dict
        '''
        res= requests.get(self.base_url + ENDPOINTS[endpoint] + "?" + parse.urlencode(params))
        
        
        return {
            "statusCode": res.status_code,
            "data": res.json()
        }

    def request_test(self, endpoint, params):
        '''
        Given endpoint of API and params returns the request response in text format.

        params: required
            endpoint: from the given dictionary of endpoints in endpoints.py
            type: str or list of str

            params: given when the function is called
            type: dict

        returns the request response in text format
                rtype: text
        '''
        res= requests.get(self.base_url + ENDPOINTS[endpoint] + "?" + parse.urlencode(params))
        
        return res.text
    
    def request_url(self, endpoint, params):
        '''
        Given endpoint of API and params returns the request's parsed url.

        params: required
            endpoint: from the given dictionary of endpoints in endpoints.py
            type: str or list of str

            params: given when the function is called
            type: dict

        returns the request's parsed url
                rtype: str
        '''
        return req.Request(self.base_url + ENDPOINTS[endpoint] + "?" + parse.urlencode(params)).get_full_url()
    