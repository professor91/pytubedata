# https://developers.google.com/youtube/v3/docs/search
from .youtube import api

class search(api):
    """
    The search class handles the methods to make search queries on Youtube using YouTube Data API

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)

    def get(self, _query, maxResults=20, **kwargs):
        '''
        Given a `query` returns information about a YouTube video, channel, or playlist that matches the search parameters.

        Read the docs: https://developers.google.com/youtube/v3/docs/search/list

        params: required
            query: The query to be searched for on Youtube
            type: str

        params: optional
            **kwargs:
                Read the docs: https://developers.google.com/youtube/v3/docs/search/list - optional parameters

        returns metadata from the inputted query ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "q": _query,
            "part": "snippet",
            "type": "video",
            "maxResults": maxResults
        }
        params.update(kwargs)
        
        return self.request("search", params)